from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from configapp.add_pagination import CustomPaginator
from configapp.models.salom import SalomBer
from configapp.serializers.salom_serializer import SalomSerializer


class SalomApi(APIView):
    @swagger_auto_schema(request_body=SalomSerializer)
    def post(self, request):
        serializer = SalomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        salom_title = SalomBer.objects.all().order_by('-id')
        paginator = CustomPaginator()
        result_page = paginator.paginate_queryset(salom_title, request)
        serializer = SalomSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
