from django.shortcuts import render,get_object_or_404
from django.views.generic import View, ListView,DetailView
from . models import Order,OrderProduct
from cart.models import Cart
from product.models import Product
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin

# api imports
from .serializer import OrderSerializer, OrderProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class OrderListAPI(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'slug'
    lookup_field = 'slug'
    queryset = Order.objects.all()