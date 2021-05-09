from django.shortcuts import render
from rest_framework import generics, views
from .serializers import DocsSerializer
from .models import SomeModel


# Create your views here.

class DocsList(generics.ListAPIView):
    queryset = SomeModel.objects.all()
    serializer_class = DocsSerializer
