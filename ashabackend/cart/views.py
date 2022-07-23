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
from .models import Cart,FavouriteProduct
from .serializer import CartSerializer,FavouriteProductSerializer


class CartList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
# 
    def get(self, request, format=None):
        print("user Id: ", self.request.user)
        cart = Cart.objects.filter(owner=self.request.user.id)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

class AddProductToCart (generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product_slug  = self.request.data.get("product", None)  # read data from request
        producttosave = Product.objects.get(slug__exact=product_slug)
        serializer.save(owner=self.request.user,product=producttosave)


class RemoveRetreiveUpdateDeleteCart(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    lookup_field = 'owner'

    def get_queryset(self):
        return Cart.objects.all().filter(owner=self.kwargs['owner'])
    
    def delete(self, request, *args, **kwargs):
        cart = Cart.objects.all().filter(owner=self.kwargs['owner'])
        if cart.count() > 0:
           cart.delete()
           return Response("cart items deleted", status=status.HTTP_204_NO_CONTENT)
        return Response("Unable to delete cart items.", status=status.HTTP_404_NOT_FOUND)


class AddProductToFavourite(generics.ListCreateAPIView):
    queryset = FavouriteProduct.objects.all()
    serializer_class = FavouriteProductSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        product_slug  = self.request.data.get("product", None)  # read data from request
        producttosave = Product.objects.get(slug__exact=product_slug)
        serializer.save(owner=self.request.user,product=producttosave)
    
    def retrieve(self,request, *args, **kwargs):
        return self.queryset.filter(owner=self.request.user)

class RemoveRetreiveUpdateDeleteFavourite(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FavouriteProductSerializer
    queryset = FavouriteProduct.objects.all()