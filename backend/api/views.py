from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from . import models, serializers


class SignUp(APIView):
    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": True})
        else:
            return Response({"status": False})


class SignIn(APIView):
    def post(self, request):
        serializer = ObtainAuthToken.serializer_class(data=request.data)

        if serializer.is_valid():
            token = Token.objects.get(user=serializer.validated_data["user"])
            return Response({"status": True, "token": token.key})
        else:
            return Response({"status": False})


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = Token.objects.get(key=request.auth)
        serializer = serializers.UserSerializer(token.user)
        return Response(serializer.data)


class RestaurantList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        restaurant_list = models.Restaurant.objects.all()
        serializer = serializers.RestaurantSerializer(
            restaurant_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        token = Token.objects.get(key=request.auth)
        serializer = serializers.RestaurantSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(vendor=token.user)
            return Response({"status": True})
        else:
            return Response({"status": False})


class RestaurantDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, restaurant_id):
        restaurant_detail = models.Restaurant.objects.get(id=restaurant_id)
        serializer = serializers.RestaurantSerializer(restaurant_detail)
        return Response(serializer.data)

    def delete(self, request, restaurant_id):
        restaurant_detail = models.Restaurant.objects.get(id=restaurant_id)
        restaurant_detail.delete()
        return Response({"status": True})


class RestaurantItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, restaurant_id):
        menu_list = models.RestaurantItem.objects.filter(
            restaurant_id=restaurant_id)
        serializer = serializers.RestaurantItemSerializer(menu_list, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_id):
        serializer = serializers.RestaurantItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(restaurant_id=restaurant_id)
            return Response({"status": True})
        else:
            return Response({"status": False})


class RestaurantItemDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, restaurant_id, restaurant_item_id):
        menu_detail = models.RestaurantItem.objects.get(
            id=restaurant_item_id, restaurant_id=restaurant_id)
        serializer = serializers.RestaurantItemSerializer(menu_detail)
        return Response(serializer.data)

    def delete(self, request, restaurant_id, restaurant_item_id):
        menu_detail = models.RestaurantItem.objects.get(
            id=restaurant_item_id, restaurant_id=restaurant_id)
        menu_detail.delete()
        return Response({"status": True})


class CartList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = Token.objects.get(key=request.auth)
        cart_list = models.Cart.objects.filter(customer=token.user)
        serializer = serializers.CartSerializer(cart_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        token = Token.objects.get(key=request.auth)
        serializer = serializers.CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(customer=token.user,
                            restaurant_id=request.data["restaurant_id"])
            return Response({"status": True})
        else:
            return Response({"status": False})


class CartDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cart_id):
        cart_detail = models.Cart.objects.get(id=cart_id)
        serializer = serializers.CartSerializer(cart_detail)
        return Response(serializer.data)

    def delete(self, request, cart_id):
        cart_detail = models.Cart.objects.get(id=cart_id)
        cart_detail.delete()
        return Response({"status": True})


class CartItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, cart_id):
        cart_item_list = models.CartItem.objects.filter(cart_id=cart_id)
        serializer = serializers.CartItemSerializer(cart_item_list, many=True)
        return Response(serializer.data)

    def post(self, request, cart_id):
        serializer = serializers.CartItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(cart_id=cart_id)
            return Response({"status": True})
        else:
            return Response({"status": False})


class OrderList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_list = models.Order.objects.all()
        serializer = serializers.OrderSerializer(order_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        token = Token.objects.get(key=request.auth)
        serializer = serializers.OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(customer=token.user)
            return Response({"status": True})
        else:
            return Response({"status": False})


class OrderDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        order_detail = models.Order.objects.get(id=order_id)
        serializer = serializers.OrderSerializer(order_detail)
        return Response(serializer.data)

    def delete(self, request, order_id):
        order_detail = models.Order.objects.get(id=order_id)
        order_detail.delete()
        return Response({"status": True})


class OrderItemList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id):
        order_item_list = models.OrderItem.objects.filter(order_id=order_id)
        serializer = serializers.OrderItemSerializer(
            order_item_list, many=True)
        return Response(serializer.data)

    def post(self, request, order_id):
        serializer = serializers.OrderItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(order_id=order_id)
            return Response({"status": True})
        else:
            return Response({"status": False})
