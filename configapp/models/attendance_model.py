from configapp.models import GroupStudent, Student
from django.db import models

class Attendance(models.Model):
    group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)
    date = models.DateField()
    lesson_name = models.CharField(max_length=255)  # Dars nomi
    descriptions = models.TextField(blank=True)

    def __str__(self):
        return f"{self.group.name} - {self.date} - {self.lesson_name}"


class StudentAttendance(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name="student_attendances")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)  # Default qiymat: False -> kelmagan

    class Meta:
        unique_together = ['attendance', 'student']

    def __str__(self):
        status = "Keldi" if self.is_present else "Kelmadi"
        return f"{self.student} - {self.attendance.date} - {status}"

# from configapp.models import GroupStudent, Student
# from django.db import models
#
# class Attendance(models.Model):
#     group = models.ForeignKey(GroupStudent, on_delete=models.CASCADE)
#     date = models.DateField()
#     descriptions = models.TextField(blank=True)
#
#     def __str__(self):
#         return f"{self.group.name} - {self.date}"
#
#
# class StudentAttendance(models.Model):
#     STATUS_CHOICES = [
#         ("bor", "Bor"),
#         ("yo'q", "Yo'q"),
#         ("kechikkan", "Kechikkan"),
#     ]
#
#     attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name="student_attendances")
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="yo'q")  # Default qiymat qo‘shildi
#
#     class Meta:
#         unique_together = ['attendance', 'student']  # Har bir student uchun bitta qatnashuv yozuvi bo‘lishi kerak
#
#     def __str__(self):
#         return f"{self.student} - {self.attendance.date} - {self.status}"