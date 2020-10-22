from django.shortcuts import render
from rest_framework import generics, status
from .models import Accounts
from .serilizers import AccountsSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class UserListAPIView(generics.ListAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

class LoginAPIView(APIView):

    permission_classes = ()

    def post(self, request):
        username = request.data["username"]
        user = User.objects.get(username=username)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)