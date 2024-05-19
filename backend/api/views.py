from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes

from . import models, serializers


@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        serializer = serializers.SignUpSerializer(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            return Response({"status": True})
        else:
            return Response({"status": False, "errors": serializer.errors})


@api_view(["POST"])
def signin(request):
    if request.method == "POST":
        serializer = ObtainAuthToken.serializer_class(data=request.data)

        if serializer.is_valid():
            token = Token.objects.get(user=serializer.validated_data["user"])
            return Response({"status": True, "token": token.key})
        else:
            return Response({"status": False})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def me(request):
    if request.method == "GET":
        token = Token.objects.get(key=request.auth)
        serializer = serializers.UserSerializer(token.user)
        return Response(serializer.data)
