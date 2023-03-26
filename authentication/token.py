import jwt
from datetime import datetime as dt, timedelta
from django.conf import settings


def get_access_token(user):

    access_token_payload = {
        'email': user.email,
        'exp': dt.now() + timedelta(days=0, minutes=5),
        'iat': dt.now()
    }

    access_token = jwt.encode(access_token_payload,settings.SECRET_KEY,algorithm=settings.ALGORITHM)

    return access_token


def get_refresh_token(user):

    refresh_token_payload = {
        'email': user.email,
        'exp': dt.now() + timedelta(days=0, minutes=30),
        'iat': dt.now()
    }

    refresh_token = jwt.encode(refresh_token_payload,settings.SECRET_KEY,algorithm=settings.ALGORITHM)

    return refresh_token
