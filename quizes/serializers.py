from .models import Quiz
from rest_framework import serializers


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'topic', 'number_of_questions', 'score')
        model = Quiz
