from rest_framework import serializers
from .models import Computer


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'kernel_version', 'product_type', 'product_version', 'processor_type', 'physical_memory',
                  'video_driver', 'created_at', 'updated_at',)
        model = Computer
