from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from .models import Computer
from .serializers import ComputerSerializer, UserSerializer
from .parsing import parsing
from django.http import JsonResponse
from .permissions import IsAuthorOrReadOnly


# Create your views here.

class ComputerList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


def start(request, *args, **kwargs):
    parsing()
    return JsonResponse({'status': 'success'})


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
