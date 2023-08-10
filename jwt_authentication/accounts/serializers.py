from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data) 
        user.set_password(password)
        user.save()

        return user

class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)