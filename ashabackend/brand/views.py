from .serializer import BrandSerilizer
from rest_framework import generics
from .models import Brand

class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerilizer


class BrandDetailView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerilizer
    lookup_field = 'slug'

