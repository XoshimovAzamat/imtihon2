from rest_framework import serializers
from ..models import *


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = "__all__"