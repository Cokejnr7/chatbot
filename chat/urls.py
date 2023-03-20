from django.urls import path
from .views import home, getPrompt

urlpatterns = [
    path('', home),
    path('prompt/', getPrompt),
]
