from rest_framework import serializers
from ..models import *
from ..models.salom import SalomBer


class SalomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalomBer
        fields = '__all__'
