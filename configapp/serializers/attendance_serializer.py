from rest_framework import serializers
from configapp.models import GroupStudent, Student  # Tashqi modellardan foydalanish uchun
from configapp.models.attendance_model import StudentAttendance, Attendance


# StudentAttendance modelining oddiy serializeri
class StudentAttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.full_name', read_only=True)  # Foydali qo‘shimcha

    class Meta:
        model = StudentAttendance
        fields = ['id', 'attendance', 'student', 'student_name', 'status']


# Attendance modelining asosiy serializeri
class AttendanceSerializer(serializers.ModelSerializer):
    group_name = serializers.CharField(source='group.name', read_only=True)  # Guruh nomi ko‘rsatish uchun
    student_attendances = StudentAttendanceSerializer(many=True, read_only=True)  # related_name orqali

    class Meta:
        model = Attendance
        fields = ['id', 'group', 'group_name', 'date', 'descriptions', 'student_attendances']
