from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, views
from rest_framework.response import Response
from .models import Computer, Application
from .serializers import ComputerSerializer, UserSerializer, ApplicationSerializer
from .parsing import parsing
from django.http import JsonResponse
from .permissions import IsAuthorOrReadOnly
from .scripts import script


# Create your views here.

class ComputerList(generics.ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class ComputerDetail(views.APIView):
    permission_classes = (IsAuthorOrReadOnly,)

    def get_object(self, title):
        return Computer.objects.get(title=title)

    def get(self, request, title):
        object = self.get_object(title)
        serializer = ComputerSerializer(object)
        return Response(serializer.data)

    serializer_class = ComputerSerializer


class ApplicationList(generics.ListAPIView):
    def get_queryset(self):
        computer = Computer.objects.get(title=self.kwargs['title'])
        return computer.applications.all()

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
