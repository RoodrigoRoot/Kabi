from django.shortcuts import render
from rest_framework import generics, status
from .models import Accounts, Company
from .serilizers import AccountsSerializer, CompanySerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from django.contrib.auth import logout
# Create your views here.


class UserListAPIView(generics.ListAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer

class CompanyListAPIView(generics.ListAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class LoginAPIView(APIView):

    permission_classes = ()

    def post(self, request):
        username = request.data["username"]
        user = User.objects.get(username=username)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)



class CompanyView(View):

    def get(self, request, *args , **kwargs):

        return render(request, 'base.html', locals())


def logout_view(request):
    logout(request)
    return redirect(reverse("home"))
