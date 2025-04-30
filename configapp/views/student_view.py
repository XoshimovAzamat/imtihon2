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

class StudentPutPatchApi(APIView):
    @swagger_auto_schema(request_body=StudentPostSerializer)
    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)

        # Foydalanuvchini yangilash
        user_data = request.data.get('user', {})
        user_serializer = StudentUserSerializer(student.user, data=user_data)
        if user_serializer.is_valid():
            # Parolni xash qilish
            if 'password' in user_serializer.validated_data:
                user_serializer.validated_data['password'] = make_password(user_serializer.validated_data['password'])
            user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Talabani yangilash
        student_data = request.data.get('student', {})
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student = student_serializer.save()

            # ManyToMany maydonlarni yangilash
            group_ids = student_data.get('group', [])
            student.group.set(group_ids)

            return Response(student_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=StudentPostSerializer)
    def patch(self, request, pk):
        student = get_object_or_404(Student, pk=pk)

        # Foydalanuvchini qisman yangilash
        user_data = request.data.get('user', {})
        if user_data:
            user_serializer = StudentUserSerializer(student.user, data=user_data, partial=True)
            if user_serializer.is_valid():
                if 'password' in user_serializer.validated_data:
                    user_serializer.validated_data['password'] = make_password(
                        user_serializer.validated_data['password'])
                user_serializer.save()
            else:
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Talabani qisman yangilash
        student_data = request.data.get('student', {})
        student_serializer = StudentSerializer(student, data=student_data, partial=True)
        if student_serializer.is_valid():
            student = student_serializer.save()

            # ManyToMany maydonlarini yangilash
            group_ids = student_data.get('group', [])
            if group_ids:
                student.group.set(group_ids)

            return Response(student_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
