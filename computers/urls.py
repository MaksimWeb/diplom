from django.urls import path
from .views import ComputerList, ComputerDetail, start

urlpatterns = [
    path('<int:pk>', ComputerDetail.as_view()),
    path('', ComputerList.as_view()),
    path('parse/', start)
]
