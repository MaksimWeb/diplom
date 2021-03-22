from .models import TestDocs
from rest_framework import serializers


class TestDocsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'document',)
        model = TestDocs
