from django.shortcuts import render
from rest_framework import generics, views
from .serializers import TestDocsSerializer, AllHistory
from .models import TestDocs
from simple_history.models import HistoricalRecords


# Create your views here.

class TestDocsList(generics.ListAPIView):
    queryset = TestDocs.objects.all()
    serializer_class = TestDocsSerializer


class AllHistoryList(generics.ListAPIView):
    queryset = TestDocs.history.all()
    serializer_class = AllHistory
