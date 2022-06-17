from .serializer import ProductSerializer
from .models import Product
from rest_framework import generics
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter



class LandingPage(TemplateView):
    template_name = "landing.html"

# Create your views here.
class ProductListview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,OrderingFilter]
    filterset_fields = ['category', 'price','brand']
    ordering_fields = ['price','created_at']
    odering = ['price']

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

