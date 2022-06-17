from .serializer import ProductSerializer
from .models import Product
from rest_framework import generics,filters
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend



class LandingPage(TemplateView):
    template_name = "landing.html"

# Create your views here.
class ProductListview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    filterset_fields = ['category', 'price','brand']
    ordering_fields = ['price','created_at']
    search_fields = ['productName', 'descripton']

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

