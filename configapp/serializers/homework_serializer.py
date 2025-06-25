from configapp.models.homework_model import Homework, HomeworkSubmission
from rest_framework import serializers


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def validate(self, attrs):
        request = self.context.get('request')
        if not request:
            raise serializers.ValidationError("Request object not found in context.")

        user = request.user
        if not user.is_authenticated or not getattr(user, "is_teacher", False):
            raise serializers.ValidationError("Only teachers can create homework.")
        return attrs


class HomeworkSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmission
        fields = '__all__'
        read_only_fields = ['student', 'submitted_at']
