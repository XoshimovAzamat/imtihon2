from rest_framework import viewsets
from ..models.attendance_model import Attendance, StudentAttendance
from ..serializers.attendance_serializer import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Attendance.objects.all().order_by('-date')
        return Attendance.objects.filter(group__teacher__user=user).order_by('-date')


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
