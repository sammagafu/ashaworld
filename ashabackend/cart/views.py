from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from product.models import Product
from .models import Cart
from .serializer import CartSerializer


class CartList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        cart = Cart.objects.filter(owner=self.request.user)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    # def post(self,request, format=None):
    #     product_slug = self.request.POST.get('product')
    #     product = Product.objects.get(slug__exact=product_slug)
    #     owner = self.request.user
    #     print(request.data)
    #     serializer = CartSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddProductToCart (generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product_slug  = self.request.data.get("product", None)  # read data from request
        producttosave = Product.objects.get(slug__exact=product_slug)
        serializer.save(owner=self.request.user,product=producttosave)
