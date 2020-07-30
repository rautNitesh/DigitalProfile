from django.contrib.auth.views import get_user_model

from rest_framework import serializers, exceptions
from rest_framework.views import Response

USER = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=150, style={ 'input_type': 'password'}, write_only=True)

    class Meta:
        model = USER
        fields = ['username', 'password', 'email', 'confirm_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        print(self.validated_data)
        user = USER(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        print(password)
        confirm_password = self.validated_data['confirm_password']
        print(confirm_password)
        if password != confirm_password:
            raise serializers.ValidationError({'error': "What an error mismatch"})
        user.set_password(password)
        user.save()

        return user
