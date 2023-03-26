from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import exceptions
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from .token import get_access_token, get_refresh_token
# Create your views here.

User = get_user_model()


class UserCreateView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')

        if email is None and password is None:
            raise exceptions.AuthenticationFailed(
                "email and password required")

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed("no user with that email")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed(f'incorrect password')

        access_token = get_access_token(user)
        refresh_token = get_refresh_token(user)

        serializer = UserSerializer(user)

        data = {
            "user": serializer.data,
            "access_token": access_token,
            "refresh_token": refresh_token
        }

        return Response(data, status=status.HTTP_200_OK)


def login(request):
    return render(request, 'authentication/login.html')


def register(request):
    return render(request, 'authentication/register.html')
