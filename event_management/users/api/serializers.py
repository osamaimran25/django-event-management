from rest_framework import serializers
from event_management.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile_number', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')  # Extract the password
        validated_data['is_active'] = True
        user = User.objects.create(**validated_data)
        user.set_password(password)  # Set the password
        user.save()
        return user

class LoginTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
