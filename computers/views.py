from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Computer, Application
from .serializers import ComputerSerializer, UserSerializer, ApplicationSerializer
from .parsing import parsing
from django.http import JsonResponse
from .permissions import IsAuthorOrReadOnly
from .scripts import script


# Create your views here.

class ComputerList(generics.ListCreateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ApplicationList(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


def start(request, *args, **kwargs):
    parsing()
    return JsonResponse({'status': 'success'})


def runScript(request, *args, **kwargs):
    script()
    return JsonResponse({'status': 'success'})


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
