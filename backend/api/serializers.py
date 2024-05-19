from rest_framework import serializers

from . import models


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username", "password", "first_name", "last_name", "role"]

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username", "first_name", "last_name", "role"]


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ["name"]


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = ["name", "price"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ["total_price"]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ["quantity", "menu_item"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ["status"]
