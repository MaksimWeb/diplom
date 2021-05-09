from django.shortcuts import render
from rest_framework import generics, views, viewsets
from rest_framework.response import Response
from .serializers import ResultSerializer, ResultsOnly
from .models import Result


class ResultList(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


class ResultsClear(generics.ListCreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultsOnly
