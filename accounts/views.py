from django.shortcuts import render
import datetime
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, smart_str

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework import exceptions
import jwt
from rest_framework import status

from DigitalProfile.settings.env import SECRET_KEY
from .authentication import TokenAuthentication
from .serializers import UserSerializer, PasswordChangeSerializer, PasswordResetSerializer, PasswordResetRequestSerializer

USER = get_user_model()


class UserLoginView(APIView):

    def post(self, request, *args, **kwargs):
        if not request.data:
            raise exceptions.AuthenticationFailed(
                {"error": "Please provide login credentials"})

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            payload = {
                "token": "access-token",
                "id": user.id,
                "email": user.email,
                "exp": datetime.datetime.now() + datetime.timedelta(minutes=1)
            }
            # print(datetime.datetime.now() + datetime.timedelta(minutes=15))
            jwt_token = {"token": jwt.encode(payload, SECRET_KEY)}

            return Response(jwt_token,
                            status=status.HTTP_200_OK)
        else:
            raise exceptions.ValidationError(
                {"error": "Invalid login credentials, please login again"})


class SignUpView(APIView):
    def post(self, request, *args, **kwargs):
        if not request.data:
            raise exceptions.AuthenticationFailed(
                {"error": "Please fill up signup form"})

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


class PasswordChangeView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeSerializer
    model = USER

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({"error": "Password incorrect"}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            print("Updated")
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeRequestView(generics.GenericAPIView):
    serializer_class = [PasswordResetRequestSerializer, ]

    def post(self, request, *args, **kwargs):
        user_email = request.data.get('email')
        try:
            print(user_email)
            user = USER.objects.get(email=user_email)
        except Exception:
            return Response({"error": "No user matching to the username found"}, status=status.HTTP_404_NOT_FOUND)
        payload = {
            "purpose": "password-reset",
            "email": user_email,
            "exp": datetime.datetime.now() + datetime.timedelta(minutes=15)
        }
        token = jwt.encode(payload, SECRET_KEY)
        current_site = get_current_site(request).domain
        relative_link = reverse('change_password_reset',
                                kwargs={'token': token})
        url = "http://" + current_site + relative_link
        body = "Dear" + user.username +\
            "please verify your identity using the link below" + url
        send_mail(subject="verify your identity", message=body,
                  from_email="rautesh6@gmail.com", recipient_list=[user_email], fail_silently=True)
        print(body)
        return Response(token)


class PasswordResetChangeView(generics.UpdateAPIView):
    serializer_class = PasswordResetSerializer

    def update(self, request, token, *args, **kwargs):
        value = token.split('\'')
        # print(value[1])
        try:
            token_user = jwt.decode(value[1], SECRET_KEY)
            user_email = token_user.get('email')
            purpose = token_user.get('purpose')
            if purpose == "password-reset":
                user = USER.objects.get(email=user_email)
                serializer = PasswordResetSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user.set_password(
                    serializer.validated_data.get('new_password'))
                user.save()
                return Response({"success": "Password reset successfully"})
            else:
                raise exceptions.AuthenticationFailed(
                    {"error": "Invalid token"}, status.HTTP_400_BAD_REQUEST)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed({"error": "The token has expired please request a new one"},
                                                  status.HTTP_400_BAD_REQUEST)
        except IndexError:
            raise exceptions.AuthenticationFailed(
                {"error": "Invalid token"}, status.HTTP_400_BAD_REQUEST)

# view for refreshing token.
# class RefreshTokenView(APIView):

#     authentication_classes = [TokenAuthentication]

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def get(self, request, *args, **kwargs):
