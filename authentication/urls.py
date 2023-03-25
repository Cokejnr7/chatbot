from django.urls import path
from .views import UserCreateView, UserLoginView, login, register

urlpatterns = [
    path('register/', UserCreateView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('signin/', login),
    path('signup/', register),
]
