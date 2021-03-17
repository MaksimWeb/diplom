
from .models import Result
from rest_framework import serializers


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('quiz', 'user', 'score', 'created')
        model = Result
