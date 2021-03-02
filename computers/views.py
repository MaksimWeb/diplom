from django.shortcuts import render
from rest_framework import generics
from .models import Computer
from .serializers import ComputerSerializer
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
