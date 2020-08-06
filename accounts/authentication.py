import jwt
from django.contrib.auth.views import get_user_model

from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions, status

from DigitalProfile.settings.env import SECRET_KEY


USER = get_user_model()

class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'token' or len(auth) == 0 or len(auth) > 2:
            raise exceptions.AuthenticationFailed({"error": "Please provide valid auth header"})

        try:
            token = auth[1]
            if token == 'null':
               raise exceptions.AuthenticationFailed({"error": "Please provide valid token"})
        except UnicodeError:
            raise exceptions.AuthenticationFailed({"error": "Invalid characters in auth header"})

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY)
            user_id = payload['id']
            email = payload['email']

            user = USER.objects.get(
                id=user_id,
                email=email,
                is_active=True,
            )
            return (user, token)

        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed({"error": "please provide valid credentials"}
                                                  , status.HTTP_401_UNAUTHORIZED)


