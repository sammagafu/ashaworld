from django.shortcuts import render,get_object_or_404
from django.views.generic import View, ListView,DetailView
from . models import Order,OrderItems
from cart.models import Cart
from product.models import Product
from django.db.models import Sum


# api imports
from .serializer import OrderSerializer, OrderProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class OrderListAPI(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,)

class OrderRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'
    queryset = Order.objects.all()

class OrderItemListAPI(generics.ListCreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user,)

class OrderItemRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderProductSerializer
    queryset = OrderItems.objects.all()