from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .models.homework_model import HomeworkSubmission
from .views import *
from .views import about_me
from .views.group_view import GroupApi, GroupStudentDetailUpdateAPIView, CourseApi, CoursePutPatchApi
from .views.homework_view import HomeworkListCreateApi, HomeworkSubmissionCreateApi
from .views.payments_view import PaymentsApi, PaymentsPutPatchApi
from .views.staff_view import StatisticsAPIView, DepartamentApi
from .views.table_view import TableApi, RoomApi, TableTypeApi

router = DefaultRouter()
# router.register('student-attendance', StudentAttendanceViewSet, basename='studentattendance')

urlpatterns = [
    path('about/', about_me, name='about_me'),
    path('contacts/', contacts, name='contacts'),

    # Student API
    path('student/', StudentApi.as_view(), name='students'),
    path('student/<int:pk>/', StudentPutPatchApi.as_view(), name='students'),
    path('student/status/', StudentStatusByDateAPIView.as_view(), name='student-status'),

    # Teacher API
    path('teacher/', TeacherApi.as_view(), name='teacher'),
    path('teacher/<int:pk>/', TeacherPutPatchApi.as_view(), name='teacher'),
    path('users/', RegisterUserApi.as_view(), name='users'),
    path('teacher/info-group/', TeacherGroupInfoAPIView.as_view(), name='teacher'),
    path('departament/', DepartamentApi.as_view(), name='departament'),
    path('', include(router.urls)),

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

    # Table API
    path('table/', TableApi.as_view(), name='tables'),
    path('table-type/', TableTypeApi.as_view(), name='table-types'),

    # Room API
    path('room/', RoomApi.as_view(), name='rooms'),


    # Payments API
    path('payments/', PaymentsApi.as_view(), name='payments'),
    path('payments/<int:pk>/', PaymentsPutPatchApi.as_view(), name='payments'),
    path('homeworks/teacher-create', HomeworkListCreateApi.as_view(), name='homework-list-create'),

    # Homework API
    path('homeworks/<int:homework_id>/submission/', HomeworkSubmissionCreateApi.as_view(),
         name='homework-submission-create'),  # homework topshirish
    # Statistika API
    path('statistic/', StatisticsAPIView.as_view(), name='statistic')
]
