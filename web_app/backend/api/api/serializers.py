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
            "role",
            "pan",
            "aadhar",
            "first_name",
            "last_name",
            "password",
        )


class CottonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CottonType
        fields = "__all__"


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Market
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    cotton_type = CottonTypeSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True, allow_null=True, source="user", queryset=User.objects.all(),
    )

    class Meta:
        model = models.Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True, allow_null=True, source="user", queryset=User.objects.all(),
    )

    class Meta:
        model = models.Order
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        allow_null=True,
        source="product",
        queryset=Product.objects.all(),
    )

    class Meta:
        model = models.Inventory
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):

    order = OrderSerializer(read_only=True)
    inventory = InventorySerializer(read_only=True)
    order_id = serializers.PrimaryKeyRelatedField(
        write_only=True, allow_null=True, source="order", queryset=Order.objects.all(),
    )
    inventory_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        allow_null=True,
        source="inventory",
        queryset=Inventory.objects.all(),
    )

    class Meta:
        model = models.OrderItem
        fields = "__all__"


class AnalysisSerializer(serializers.ModelSerializer):

    cotton_type = CottonTypeSerializer(read_only=True)
    market = MarketSerializer(read_only=True)

    class Meta:
        model = models.Analysis
        fields = "__all__"


class FrequentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FrequentQuestion
        fields = "__all__"


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complain
        fields = "__all__"


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Opinion
        fields = "__all__"

