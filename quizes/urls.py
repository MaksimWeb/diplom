from django.urls import path
from .views import QuizList

urlpatterns = [
    path('', QuizList.as_view()),
]
