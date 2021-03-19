from django.urls import path
from .views import ResultList, ResultsClear

urlpatterns = [
    path('', ResultList.as_view()),
    path('set-results/', ResultsClear.as_view()),
]
