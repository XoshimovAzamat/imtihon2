from django.contrib.auth.hashers import make_password
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from ..add_pagination import CustomPaginator
from ..models import Student, User
from django.shortcuts import get_object_or_404
from ..serializers import StudentSerializer, StudentUserSerializer, StudentPostSerializer


class StudentApi(APIView):
    @swagger_auto_schema(request_body=StudentPostSerializer)
    def post(self, request):
        data = {"success": True}
        user_data = request.data['user']
        student_data = request.data['student']

        user_serializer = StudentUserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)

        validated_user = user_serializer.validated_data
        validated_user['password'] = make_password(validated_user['password'])
        validated_user['is_student'] = True
        validated_user['is_active'] = True

        user = User.objects.create(**validated_user)

        student_serializer = StudentSerializer(data=student_data)
        student_serializer.is_valid(raise_exception=True)

        student = student_serializer.save(user=user)

        if 'departments' in student_data:
            student.departments.set(student_data['departments'])
        if 'course' in student_data:
            student.course.set(student_data['course'])

        data['user'] = StudentUserSerializer(user).data
        data['student'] = StudentSerializer(student).data
        return Response(data)

    def get(self, request):
        students = Student.objects.all().order_by('-id')
        paginator = CustomPaginator()
        paginator.page_size = 2
        result_page = paginator.paginate_queryset(students, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
