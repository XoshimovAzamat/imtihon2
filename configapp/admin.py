from django.contrib import admin

from configapp.models import *

admin.site.register([Teacher, User, Student, GroupStudent, Departments, Course])
