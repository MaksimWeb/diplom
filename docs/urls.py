from django.urls import path
from .views import DocsList

urlpatterns = [
    path('doc/', DocsList.as_view())
]
