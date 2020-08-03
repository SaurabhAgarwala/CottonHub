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
import base64


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


@permission_classes([IsAuthenticated])
class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


@permission_classes([IsAuthenticated])
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer

    @list_route(methods=["get"])
    def me(self, request, **kwargs):
        user = request.user
        print(user)
        order = Order.objects.filter(user=user)
        print(order)
        order_items = OrderItem.objects.filter(order__in=order)
        print(order_items)
        order_items_serializer = serializers.OrderItemSerializer(
            order_items, many=True
        ).data
        return Response(order_items_serializer)


class CottonTypeViewSet(viewsets.ModelViewSet):
    queryset = models.CottonType.objects.all()
    serializer_class = serializers.CottonTypeSerializer


class MarketViewSet(viewsets.ModelViewSet):
    queryset = models.Market.objects.all()
    serializer_class = serializers.MarketSerializer


@permission_classes([IsAuthenticated])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


@permission_classes([IsAuthenticated])
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = models.Inventory.objects.all()
    serializer_class = serializers.InventorySerializer

    @list_route(methods=["get"])
    def me(self, request, **kwargs):
        user = request.user
        product = Product.objects.filter(user=user)
        inventory = Inventory.objects.filter(product__in=product)
        inventory_serializer = serializers.InventorySerializer(
            inventory, many=True
        ).data
        return Response(inventory_serializer)


# Analysis.objects.filter(
#                 cotton_type__in=CottonType.objects.filter(name='Cotton'),
#                 market__in=Market.objects.filter(name='Adilabad'),
#             )


@permission_classes([IsAuthenticated])
class AnalysisViewSet(viewsets.ModelViewSet):
    queryset = models.Analysis.objects.all()
    serializer_class = serializers.AnalysisSerializer

    @list_route(methods=["get"])
    def specific(self, request, **kwargs):
        market = request.GET.get("market", "")
        cottontype = request.GET.get("cottontype", "")
        if market != "" and cottontype != "":
            analysis_data = Analysis.objects.filter(
                cotton_type__in=CottonType.objects.filter(id=cottontype),
                market__in=Market.objects.filter(id=market),
            )
        elif market != "":
            analysis_data = Analysis.objects.filter(
                market__in=Market.objects.filter(id=market),
            )
        else:
            analysis_data = Analysis.objects.filter(
                cotton_type__in=CottonType.objects.filter(id=cottontype),
            )
        analysis_data_extracted = serializers.AnalysisSerializer(
            analysis_data, many=True
        ).data
        return Response(analysis_data_extracted)


@api_view(["POST"])
@parser_classes((JSONParser,))
@permission_classes([IsAuthenticated])
def addToCart(request):

    data = request.data
    print(data)
    user = User.objects.get(id=data["user_uid"])
    cottontype = CottonType.objects.get(id=data["cotton_type"])
    inventory = Inventory.objects.get(id=data["inventory_id"])
    quantity = int(data["quantity"])

    order = Order(
        user=user,
        name=data["name"],
        mobile=data["mobile"],
        shipping_address=data["shipping_address"],
    )
    order.save()

    order_item = OrderItem(order=order, inventory=inventory, quantity=quantity)
    order_item.save()

    response_data = {"status": True, "order_id": order.id}

    return Response(data=response_data, status=status.HTTP_200_OK)


@api_view(["POST"])
@parser_classes((JSONParser,))
@permission_classes([IsAuthenticated])
def sellCottonProduct(request):

    data = request.data
    print(data)
    user = User.objects.get(id=data["user_uid"])
    cottontype = CottonType.objects.get(id=data["cotton_type"])
    product = Product.objects.create(user=user, cotton_type=cottontype)

    inventory = Inventory(
        product=product,
        quantity=int(data["quantity"]),
        selling_price=int(data["selling_price"]),
        msp=100,
    )

    inventory.save()

    response_data = {"status": True}

    return Response(data=response_data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def placeOrder(request, id):
    order = Order.objects.get(id=id)
    orderitem = OrderItem.objects.get(order=order)
    orderitem.inventory.quantity = orderitem.quantity
    order.purchased = True
    order.save()

    response_data = {"status": True}
    return Response(data=response_data)


class FrequentQuestionViewSet(viewsets.ModelViewSet):
    queryset = models.FrequentQuestion.objects.all()
    serializer_class = serializers.FrequentQuestionSerializer


class ComplainViewSet(viewsets.ModelViewSet):
    queryset = models.Complain.objects.all()
    serializer_class = serializers.ComplainSerializer


class OpinionViewSet(viewsets.ModelViewSet):
    queryset = models.Opinion.objects.all()
    serializer_class = serializers.OpinionSerializer

@api_view(['GET'])
def getHeatMap(request):
    print(request.GET)
    state = request.GET.get("state")
    year = request.GET.get("year")
    print(state, year)
    print('static/image/heatmap_'+state+"_"+year+'.png')
    image = open('static/image/heatmap_'+state+"_"+year+'.png', 'rb') #open binary file in read mode
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read)

    data = {
        "image": image_64_encode
    }

    return Response(data)

    