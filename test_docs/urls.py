from django.urls import path
from .views import TestDocsList, AllHistoryList

urlpatterns = [
    path('', TestDocsList.as_view()),
    path('history', AllHistoryList.as_view())
]
