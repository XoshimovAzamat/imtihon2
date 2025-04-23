from django.contrib import admin

from configapp.models import *

admin.site.register([Teacher, User, Student, GroupStudent, Departments, Course, Room, Table, TableType])
# from django.contrib import admin
# from configapp.models import *
#
#
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ['user', 'departments', 'course', 'descriptions']
#     search_fields = ['user__phone_number', 'departments__name', 'course__name']
#
#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['phone_number', 'is_active', 'is_staff']
#     search_fields = ['phone_number']
#
#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'group', 'enrollment_date']
#     search_fields = ['user__phone_number']
#
#
# class GroupStudentAdmin(admin.ModelAdmin):
#     list_display = ['title', 'course', 'teacher']
#     search_fields = ['title', 'course__name', 'teacher__user__phone_number']
#
#
# class DepartmentsAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     search_fields = ['name']
#
#
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['name', 'department']
#     search_fields = ['name', 'department__name']
#
#
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ['name', 'capacity']
#     search_fields = ['name']
#
#
# class TableAdmin(admin.ModelAdmin):
#     list_display = ['room', 'table_type']
#     search_fields = ['room__name', 'table_type__name']
#
#
# class TableTypeAdmin(admin.ModelAdmin):
#     list_display = ['name']
#     search_fields = ['name']
#
#
# admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(User, UserAdmin)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(GroupStudent, GroupStudentAdmin)
# admin.site.register(Departments, DepartmentsAdmin)
# admin.site.register(Course, CourseAdmin)
# admin.site.register(Room, RoomAdmin)
# admin.site.register(Table, TableAdmin)
# admin.site.register(TableType, TableTypeAdmin)
