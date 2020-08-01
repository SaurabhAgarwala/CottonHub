from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
    parser_classes,
    list_route,
)
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import *
from . import serializers
from . import models
from rest_framework.authtoken.models import Token
from rest_framework import viewsets

import random
import requests
import json


def generateOtp():

    otp = random.randint(100000, 999999)
    return otp


@api_view(["POST"])
@parser_classes((JSONParser,))
def otpLogin(request):

    username = request.data["username"]
    phone_relation = User.objects.get(username=username)

    print(phone_relation)
    otp = generateOtp()

    try:
        otpObj = PhoneOtp.objects.get(phone_relation=phone_relation)
        otpObj.otp = otp
        otpObj.count = otpObj.count + 1
        otpObj.save()
    except:
        otpObj = PhoneOtp()
        otpObj.phone_relation = phone_relation
        otpObj.otp = otp
        otpObj.count = otpObj.count + 1
        otpObj.save()

    sendOTPToPhone(otp, username)

    data = {"message": "OTP has been send to phone number"}

    return Response(data=data, status=status.HTTP_200_OK)


def sendOTPToPhone(otp, username):

    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {
        "authorization": "8H60wA5oqnyztR1XebZ9TWIJELGvVChUiS2O7KQmPlrF4pYDcuv6n8l523iAPGwMLQmEaW14gfrRdBeJ",
        "sender_id": "FSTSMS",
        "language": "english",
        "route": "qt",
        "numbers": username,
        "message": "32413",
        "variables": "{BB}",
        "variables_values": otp,
    }

    headers = {"cache-control": "no-cache"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


@api_view(["POST"])
@parser_classes((JSONParser,))
def verifyOTP(request):

    username = request.data["username"]
    otp = request.data["otp"]

    print(username, otp)

    phone_relation = User.objects.get(username=username)
    otpObj = PhoneOtp.objects.get(phone_relation=phone_relation)

    print(otpObj.otp)

    if otpObj.otp == otp:
        otpObj.delete()
        print(phone_relation.username)
        print(phone_relation.password)
        user = User.objects.get(username=username)
        token = Token.objects.get_or_create(user=user)
        print(token)
        data = {"auth_token": token[0].key}
        return Response(data=data, status=status.HTTP_200_OK)

    else:
        data = {"message": "Incorrect OTP"}
        return Response(data=data, status=status.HTTP_406_NOT_ACCEPTABLE)
