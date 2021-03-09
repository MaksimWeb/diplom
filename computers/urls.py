from django.urls import path
from .views import UserList, UserDetail, ComputerList, ComputerDetail, start, runScript, ApplicationList

urlpatterns = [
    path('<str:title>', ComputerDetail.as_view()),
    path('', ComputerList.as_view()),
    path('applications/<str:title>', ApplicationList.as_view()),
    path('parse/', start),
    path('script/', runScript),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
