from rest_framework import serializers
from configapp.models import GroupStudent, Student


# Talaba uchun oddiy serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'user', 'descriptions']


# Davomat serializer


# Guruh serializer: ichida studentlar va davomatlar
class GroupStudentDetailSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    attendances = serializers.SerializerMethodField()

    class Meta:
        model = GroupStudent
        fields = ['id', 'title', 'start_date', 'finish_date', 'students', 'attendances']

    def get_students(self, obj):
        # Guruhga tegishli studentlarni ko‘rsatish
        students = Student.objects.filter(group=obj)
        return StudentSerializer(students, many=True).data

    def get_attendances(self, obj):
        # Shu guruhga tegishli attendance lar
        attendance = Attendance.objects.filter(group=obj)
        return AttendanceSerializer(attendance, many=True).data
