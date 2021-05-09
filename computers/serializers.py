from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Computer, Application


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'kernel_version', 'product_type', 'product_version', 'processor_type', 'physical_memory',
                  'video_driver', 'created_at', 'updated_at',)
        model = Computer


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('application_name', 'application_version')
        model = Application


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


