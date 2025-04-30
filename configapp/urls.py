from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .models.homework_model import HomeworkSubmission
from .views import *
from .views.attendance_view import AttendanceApi, AttendancePatchDeleteApi, StudentAttendanceApi, \
    StudentAttendancePutPatchDeleteApi
from .views.group_view import GroupApi, GroupStudentDetailUpdateAPIView, CourseApi, CoursePutPatchApi
from .views.homework_view import HomeworkListCreateApi, HomeworkSubmissionCreateApi
from .views.payments_view import PaymentsApi, PaymentsPutPatchApi

router = DefaultRouter()
# router.register('student-attendance', StudentAttendanceViewSet, basename='studentattendance')

urlpatterns = [
    path('student/', StudentApi.as_view(), name='students'),
    path('student/<int:pk>/', StudentPutPatchApi.as_view(), name='students'),
    path('teacher/', TeacherApi.as_view(), name='teacher'),
    path('teacher/<int:pk>/', TeacherPutPatchApi.as_view(), name='teacher'),
    path('users/', RegisterUserApi.as_view(), name='users'),
    path('', include(router.urls)),  # ✅
    # Auth API
    path('login/', LoginApi.as_view(), name='register-page'),
    path('logout/', LogoutApi.as_view(), name='logout'),
    path('register/', RegisterUserApi.as_view(), name='register-page'),
    path('send-sms/', PhoneSendOTP.as_view(), name='register-page'),
    path('verify-sms/', VerifySMS.as_view(), name='register-page'),
    # Group API
    path('group/', GroupApi.as_view(), name='groups'),
    path('group/<int:pk>/', GroupStudentDetailUpdateAPIView.as_view(), name='groups'),
    path('course/', CourseApi.as_view(), name='course'),
    path('course/<int:pk>/', CoursePutPatchApi.as_view(), name='course'),
    #Attendance API
    path('attendance/', AttendanceApi.as_view(), name='attendance'),
    path('attendance/<int:pk>/', AttendancePatchDeleteApi.as_view(), name='attendance'),
    path('student-attendance/', StudentAttendanceApi.as_view()),
    path('student-attendance/<int:pk>/', StudentAttendancePutPatchDeleteApi.as_view()),
    # Payments API
    path('payments/', PaymentsApi.as_view(), name='payments'),
    path('payments/<int:pk>/', PaymentsPutPatchApi.as_view(), name='payments'),
    path('homeworks/teacher-create', HomeworkListCreateApi.as_view(), name='homework-list-create'),# homeworklar ro'yxati va yaratish
    path('homeworks/<int:homework_id>/submission/', HomeworkSubmissionCreateApi.as_view(),name='homework-submission-create'),  # homework topshirish

]
