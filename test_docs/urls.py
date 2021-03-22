from django.urls import path
from .views import TestDocsList

urlpatterns = [
    path('', TestDocsList.as_view())
]
