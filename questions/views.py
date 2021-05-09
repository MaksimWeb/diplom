from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Answer


# Create your views here.

class QuestionList(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerList(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
