from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *
from .views.attendance_view import AttendanceViewSet, StudentAttendanceViewSet

router = DefaultRouter()
router.register('attendance', AttendanceViewSet, basename='attendance')
router.register('student-attendance', StudentAttendanceViewSet, basename='studentattendance')

urlpatterns = [
    # path('student/', StudentApi.as_view()),
    path('student/<int:pk>/', StudentApi.as_view(), name='student-detail'),
    # path('teacher/create/', TeacherCreateApi.as_view(), name='teacher'),
    path('teacher/<int:pk>/', TeacherApi.as_view(), name='teacher'),
    path('users/', RegisterUserApi.as_view(), name='users'),
    path('', include(router.urls)),  # ✅
]
