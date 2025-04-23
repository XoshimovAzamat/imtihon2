from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *
from .views.attendance_view import AttendanceViewSet, StudentAttendanceViewSet
from .views.group_view import GroupApi, GroupStudentDetailUpdateAPIView, CourseApi

router = DefaultRouter()
router.register('attendance', AttendanceViewSet, basename='attendance')
router.register('student-attendance', StudentAttendanceViewSet, basename='studentattendance')

urlpatterns = [
    path('student/', StudentApi.as_view(), name='students'),
    # path('student/<int:pk>/', StudentApi.as_view(), name='student-detail'),
    # path('teacher/create/', TeacherCreateApi.as_view(), name='teacher'),
    path('teacher/<int:pk>/', TeacherApi.as_view(), name='teacher'),
    path('users/', RegisterUserApi.as_view(), name='users'),
    path('', include(router.urls)),  # ✅
    # Auth API
    path('login/', LoginApi.as_view(), name='register-page'),
    path('register/', RegisterUserApi.as_view(), name='register-page'),
    path('send-sms/', PhoneSendOTP.as_view(), name='register-page'),
    path('verify-sms/', VerifySMS.as_view(), name='register-page'),
    # Group API
    path('group/', GroupApi.as_view(), name='groups'),
    path('group/', GroupStudentDetailUpdateAPIView.as_view(), name='groups'),
    path('course/', CourseApi.as_view(), name='course'),


]
