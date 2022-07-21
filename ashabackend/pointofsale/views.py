import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_csv import renderers as r

from . models import POSclient,POSorder,POSproduct
from .serializer import POSclientSerializer,POSproductSerializer,POSorderSerializer

class PosclientViewSet(viewsets.ModelViewSet):
     queryset = POSclient.objects.all()
     serializer_class = POSclientSerializer
     http_method_names = ['get','post','retrieve','put','patch']


class OrderRenderer (r.CSVRenderer):
    header = ['buyer.clients', 'buyer.phone_number', 'products', 'seller']

class OrderListRenderer (r.CSVRenderer):
    header = ['id','buyer.clients', 'buyer.phone_number', 'products', 'seller']

class PosOrderViewSet(viewsets.ModelViewSet):
     queryset = POSorder.objects.all()
     serializer_class = POSorderSerializer
     http_method_names = ['get','post','retrieve','put','patch','delete'] 
     
     @action(detail=True, methods=['get'], renderer_classes=(OrderRenderer, ))
     def export_order(self, request, pk=None):
          order = POSorder.objects.filter(id=request.query_params['id'])
          prods= json.loads(order[0].products)
          print('prods: ',prods)
          prod_names = [i['productName'] for i in prods]
          serializer = POSorderSerializer(order, many=True)
          serializer.data[0]['products'] = ','.join(prod_names)
          print(serializer.data[0]['products'])
          return Response(serializer.data)

     @action(detail=False, methods=['get'], renderer_classes=(OrderListRenderer, ))
     def export_order_list(self, request, pk=None):
          order = POSorder.objects.filter(seller_id=request.query_params['id'])
          # prods= json.loads(order[0].products)
          # print('prods: ',prods)
          # prod_names = [i['productName'] for i in prods]
          serializer = POSorderSerializer(order, many=True)
          # serializer.data[0]['products'] = ','.join(prod_names)
          # print(serializer.data[0]['products'])
          return Response(serializer.data)



class PosProductViewSet(viewsets.ModelViewSet):
     queryset = POSproduct.objects.all()
     serializer_class = POSproductSerializer
     http_method_names = ['get','post','retrieve','put','patch']

