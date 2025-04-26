from rest_framework import viewsets
from ..models.attendance_model import Attendance, StudentAttendance
from ..serializers.attendance_serializer import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Attendance.objects.all().order_by('-date')

        # Agar foydalanuvchi Teacher bo'lsa, u faqat o'zining guruhlarini ko'rishi kerak
        teacher = Teacher.objects.filter(user=user).first()
        if teacher:
            # Teacher o'zining guruhlari bilan bog'langan guruhlar orqali filtrlaydi
            return Attendance.objects.filter(group__teacher=teacher).order_by('-date')

        # Agar boshqa foydalanuvchi bo'lsa, faqat o'ziga tegishli guruhlar
        return Attendance.objects.filter(group__teacher__user=user).order_by('-date')

    def create(self, request, *args, **kwargs):
        # Attendance yaratish uchun serializerni tekshirish
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Yangi Attendance obyekti saqlanadi
        attendance = serializer.save()

        # Guruhga tegishli barcha talabalarni olish (students)
        students = attendance.group.get_student.all()  # ManyToManyField orqali talabalarni olish

        # Har bir talaba uchun StudentAttendance yaratish
        for student in students:
            StudentAttendance.objects.create(
                attendance=attendance,
                student=student,
                is_present=False  # Avvaliga barcha talabalar uchun kelmagan deb belgilaymiz
            )

        # Yangi yaratilgan Attendance obyektini qaytarish
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StudentAttendance.objects.all()
    serializer_class = StudentAttendanceSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return StudentAttendance.objects.all()

        return StudentAttendance.objects.filter(
            attendance__group__teacher__user=user
        )
