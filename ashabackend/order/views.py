from . models import Order,OrderItems
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_csv import renderers as r
# api imports
from .serializer import OrderSerializer, OrderProductSerializer
from rest_framework import viewsets


class OrderListRenderer(r.CSVRenderer):
    header = ['id','owner.email', 'orderstatus', 'promocode', 'totalprice']

class OrderDetailsRenderer(r.CSVRenderer):
     header = ['id','product.productName', 'order', 'quantity'] 


class OrderViewSet(viewsets.ModelViewSet):
     queryset = Order.objects.all()
     serializer_class = OrderSerializer
     http_method_names = ['get','post','retrieve','put','patch']

     @action(detail=False, methods=['get'], renderer_classes=(OrderListRenderer, ))
     def export_order_list(self, request, pk=None):
          order = Order.objects.filter(owner=request.query_params['id'])
          serializer = OrderSerializer(order, many=True)
          return Response(serializer.data)

     @action(detail=False, methods=['get'], renderer_classes=(OrderDetailsRenderer, ))
     def export_order(self, request, pk=None):
          items = OrderItems.objects.filter(order=request.query_params['order'])
          serializer = OrderProductSerializer(items, many=True)
          return Response(serializer.data)
