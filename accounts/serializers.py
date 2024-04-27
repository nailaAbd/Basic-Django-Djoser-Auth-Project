from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from accounts.twilio_utils import send_verification_code


User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    phone_number = serializers.CharField(max_length=20, required=True)
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('first_name', 'last_name', 'phone_number')
    

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # send a verification code to the user's phone number
        verification_sid = send_verification_code(validated_data['phone_number'])
        user.phone_number = validated_data['phone_number']
        user.save()
        return user


class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
