from django.urls import path
from .views import QuestionList, QuestionDetail, AnswerList

urlpatterns = [
    path('', QuestionList.as_view()),
    path('<int:pk>', QuestionDetail.as_view()),
    path('answers/', AnswerList.as_view()),
]
