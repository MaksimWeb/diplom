from .models import Question, Answer
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'quiz', 'created',)
        model = Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('text', 'correct', 'question', 'created',)
        model = Answer
