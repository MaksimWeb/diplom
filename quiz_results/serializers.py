from .models import Result
from quizes.models import Quiz
from django.contrib.auth import get_user_model
from rest_framework import serializers


class QuizS(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'topic',)


class UserS(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


class ResultSerializer(serializers.ModelSerializer):
    quiz = QuizS(read_only=True)
    user = UserS(read_only=True)

    class Meta:
        fields = ('quiz', 'user', 'score', 'created')
        model = Result


class ResultsOnly(serializers.ModelSerializer):
    class Meta:
        fields = ('quiz', 'user', 'score', 'created')
        model = Result
