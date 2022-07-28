from django.http import Http404
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Product
# from category.models import ProuctCategory
# from rest_framework import generics,filters
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework_csv import renderers as r
# from django.views.generic import TemplateView
# from django_filters.rest_framework import DjangoFilterBackend



# class LandingPage(TemplateView):
#     template_name = "landing.html"

# # Create your views here.
# class ProductListview(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
#     filterset_fields = ['category', 'price','brand']
#     ordering_fields = ['price','created_at']
#     search_fields = ['productName', 'descripton']

# class ProductDetailView(APIView):
#     def get_object(self, category_slug, product_slug):
#         try:
#             return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
#         except Product.DoesNotExist:
#             raise Http404
    
#     def get(self, request, category_slug, product_slug, format=None):
#         product = self.get_object(category_slug, product_slug)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)


class GetProductsByCategory(APIView):
    def get_object(self, category_slug):
        try:
            return Product.objects.filter(category__slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        product = self.get_object(category_slug)
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)

class ProductListRenderer(r.CSVRenderer):
     header = ['id','productName', 'price', 'sku'] 

class ProductViewSet(viewsets.ModelViewSet):
     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     http_method_names = ['get','post','retrieve','put','patch','delete']

     @action(detail=False, methods=['get'], renderer_classes=(ProductListRenderer, ))
     def export_product_list(self, request, pk=None):
          order = Product.objects.all()
          serializer = ProductSerializer(order, many=True)
          return Response(serializer.data)