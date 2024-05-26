from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username", "password", "first_name", "last_name", "role"]

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ["name"]


class RestaurantItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RestaurantItem
        fields = ["name", "price"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = ["total_price"]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ["quantity", "restaurant_item"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ["price", "status"]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ["price", "quantity", "restaurant_item"]
