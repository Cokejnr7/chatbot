from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
import jwt

User = get_user_model()


class JWTAuthentication(authentication.BasicAuthentication):
    def authenticate(self, request):
        auth = authentication.get_authorization_header(request)

        if not auth:
            return

        prefix, token = auth.decode('utf-8').split(" ")

        try:
            payload = jwt.decode(token,
                                 settings.SECRET_KEY,
                                 algorithms=[
                                     settings.ALGORITHM,
                                 ])
            user = User.objects.get(email=payload['email'])

            return (user, token)

        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("invalid token")

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("token expired")
