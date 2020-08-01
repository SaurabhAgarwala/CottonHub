from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *
from . import models


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            "id",
            "username",
            "email",
            "pan",
            "aadhar",
            "first_name",
            "last_name",
            "password",
        )
