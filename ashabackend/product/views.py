from .serializer import ProductSerializer
from .models import Product
from rest_framework import generics
from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = "landing.html"

# Create your views here.
class ProductListview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

