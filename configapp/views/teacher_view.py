from ftplib import error_temp
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from configapp.models import Teacher
from configapp.serializers import TeacherSerializer
from ..add_pagination import CustomPaginator
from django.shortcuts import get_object_or_404
from ..serializers.teacher_serializer import TeacherSerializer, TeacherPostSerializer, TeacherUserSerializer
from ..models import User


# class TeacherCreateApi(APIView):
#     @swagger_auto_schema(request_body=TeacherSerializer)
#     def post(self, request):
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": True, "detail": "Teacher created"})
#         return Response({"status": False, "errors": serializer.errors}, status=400)
#

class TeacherApi(APIView):
    @swagger_auto_schema(request_body=TeacherPostSerializer)
    def post(self, request):
        data = {"success": True}
        user_data = request.data['user']
        teacher_data = request.data['teacher']

        user_serializer = TeacherUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)

        validated_user = user_serializer.validated_data
        validated_user['password'] = make_password(validated_user['password'])
        validated_user['is_teacher'] = True
        validated_user['is_active'] = True

        user = User.objects.create(**validated_user)

        teacher_serializer = TeacherSerializer(data=teacher_data)
        teacher_serializer.is_valid(raise_exception=True)

        teacher = teacher_serializer.save(user=user)

        if 'departments' in teacher_data:
            teacher.departments.set(teacher_data['departments'])
        if 'course' in teacher_data:
            teacher.course.set(teacher_data['course'])

        data['user'] = TeacherUserSerializer(user).data
        data['teacher'] = TeacherSerializer(teacher).data
        return Response(data)

    def get(self, request):
        teachers = Teacher.objects.all().order_by('-id')
        paginator = CustomPaginator()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(teachers, request)
        serializer = TeacherSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(request_body=TeacherSerializer)
    def put(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TeacherSerializer)
    def patch(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
