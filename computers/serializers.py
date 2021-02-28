from rest_framework import serializers
from .models import Computer


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'created_at', 'updated_at',)
        model = Computer
