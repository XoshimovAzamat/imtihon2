from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
# router.register('students', StudentApi, basename='students')

urlpatterns = [
    # path('student/', StudentApi.as_view()),
    path('student/<int:pk>/', StudentApi.as_view(), name='student-detail'),
    # path('teacher/create/', TeacherCreateApi.as_view(), name='teacher'),
    path('teacher/<int:pk>/', TeacherApi.as_view(), name='teacher'),
    path('users/', RegisterUserApi.as_view(), name='users'),
    # path('', include(router.urls)),  # ✅
]
