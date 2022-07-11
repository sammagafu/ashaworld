from django.shortcuts import render,get_object_or_404
from django.views.generic import View, ListView,DetailView
from . models import Order,OrderItems
from cart.models import Cart
from product.models import Product
from django.db.models import Sum
from rest_framework import status, authentication, permissions


# api imports
from .serializer import OrderSerializer, OrderProductSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


# class OrderListCreateAPI(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     # authentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         print(self.request.data.get("product", None))
#         serializer.save(owner=self.request.user)

# class OrderRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderSerializer
#     lookup_url_kwarg = 'slug'
#     lookup_field = 'slug'
#     queryset = Order.objects.all()

# class OrderItemListAPI(generics.CreateAPIView):
#     queryset = OrderItems.objects.all()
#     serializer_class = OrderProductSerializer
#     # authentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         product_slug  = self.request.data.get("product", None)  # read data from request
#         producttosave = Product.objects.get(slug__exact=product_slug)
#         serializer.save(product=producttosave,)

# class OrderItemRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderProductSerializer
#     queryset = OrderItems.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
     queryset = Order.objects.all()
     serializer_class = OrderSerializer
     http_method_names = ['get','post','retrieve','put','patch']
