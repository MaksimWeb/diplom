from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import QuizSerializer
from .models import Quiz


# Create your views here.

class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
