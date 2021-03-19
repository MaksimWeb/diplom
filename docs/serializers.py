from .models import SomeModel
from rest_framework import serializers


class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'document',)
        model = SomeModel
