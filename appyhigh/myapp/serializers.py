from rest_framework import serializers
from common.messages import REQUIRED, EMAIL_VALID
from common.validations import validate_password, validate_email, validate_forgot_password_email, validate_phone_number
from django.contrib.auth.hashers import make_password
from .models import User, Food


class RegisterSerializer(serializers.Serializer):
    fullname = serializers.CharField(
        max_length=50, error_messages={'blank': REQUIRED})
    email = serializers.EmailField(max_length=30, error_messages={'blank': REQUIRED, 'invalid': EMAIL_VALID},
                                   validators=[validate_email])
    password = serializers.CharField(max_length=12, error_messages={
                                     'blank': REQUIRED}, validators=[validate_password])

    access_token = serializers.CharField(max_length=255, default="")

    def validate(self, attrs):
        attrs['email'] = attrs['email'].lower()
        return attrs


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        error_messages={'blank': REQUIRED, 'invalid': EMAIL_VALID})
    password = serializers.CharField(max_length=12, error_messages={
        'blank': REQUIRED}, validators=[validate_password])

    def validate(self, attrs):
        attrs['email'] = attrs['email'].lower()
        return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(error_messages={
        'blank': REQUIRED, 'invalid': EMAIL_VALID}, validators=[validate_forgot_password_email])


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('fullname', 'birth_year', 'email', 'username')


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('name', 'carbohydrates_amount',
                  'fats_amount', 'proteins_amount')
