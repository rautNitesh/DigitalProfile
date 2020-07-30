from django.shortcuts import render
import datetime
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework import exceptions
import jwt
from rest_framework import status

from DigitalProfile.settings.env import SECRET_KEY
from .serializers import UserSerializer

USER = get_user_model()


class UserLoginView(APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            raise exceptions.AuthenticationFailed({"error": "Please provide login credentials"})

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            payload = {
                "id": user.id,
                "email": user.email,
                "exp": datetime.datetime.now() + datetime.timedelta(minutes=1)
            }

            jwt_token = {"token": jwt.encode(payload, SECRET_KEY)}

            return Response(jwt_token,
                            status=status.HTTP_200_OK)
        else:
            raise exceptions.ValidationError({"error": "Invalid login credentials, please login again"})


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

    def authenticate_header(self, request):
        return 'Token'


class SignUpView(APIView):
    def post(self, request, *args, **kwargs):
        if not request.data:
            raise exceptions.AuthenticationFailed({"error": "Please fill up signup form"})

        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['success'] = "You are sign up successfully"
            data['username'] = user.username
            data['email'] = user.email
            data['user_id'] = user.id
        else:
            data = serializer.errors

        return Response(data)


class SimpleView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'logged_in': 'Hello'})

