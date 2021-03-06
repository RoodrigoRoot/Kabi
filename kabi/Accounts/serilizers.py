from rest_framework import serializers
from .models import Accounts, Company
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username",)



class AccountsSerializer(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Accounts
        fields = ("user", "phone", "direction")

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ("name", "phone", "direction")