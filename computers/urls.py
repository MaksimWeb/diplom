from django.urls import path
from .views import UserList, UserDetail, ComputerList, ComputerDetail, start

urlpatterns = [
    path('<int:pk>', ComputerDetail.as_view()),
    path('', ComputerList.as_view()),
    path('parse/', start),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
