from django.urls import path
from .views import ResultList

urlpatterns = [
    path('', ResultList.as_view()),
]
