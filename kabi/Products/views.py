from django.shortcuts import render
from .serializers import ProductSerializers
from rest_framework import generics
from .models import Product
# Create your views here.

class ProductListAPIView(generics.ListCreateAPIView):

    def get_queryset(self):
        return Product.objects.filter(active=True)
    
    serializer_class = ProductSerializers



class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()