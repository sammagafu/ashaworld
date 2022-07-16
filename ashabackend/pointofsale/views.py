from rest_framework import viewsets
from . models import POSclient,POSorder,POSproduct, ProductQuantity
from .serializer import POSclientSerializer,POSproductSerializer,POSorderSerializer,POSProductQuantitySerializer

class PosclientViewSet(viewsets.ModelViewSet):
     queryset = POSclient.objects.all()
     serializer_class = POSclientSerializer
     http_method_names = ['get','post','retrieve','put','patch']

class PosOrderViewSet(viewsets.ModelViewSet):
     queryset = POSorder.objects.all()
     serializer_class = POSorderSerializer
     http_method_names = ['get','post','retrieve','put','patch']

class PosProductViewSet(viewsets.ModelViewSet):
     queryset = POSproduct.objects.all()
     serializer_class = POSproductSerializer
     http_method_names = ['get','post','retrieve','put','patch']

class PosProductQuantityViewSet(viewsets.ModelViewSet):
     queryset = ProductQuantity.objects.all()
     serializer_class = POSProductQuantitySerializer