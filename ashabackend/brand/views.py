from .serializer import BrandSerilizer
from rest_framework import generics,viewsets
from .models import Brand

class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerilizer


class BrandDetailView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerilizer
    lookup_field = 'id'

class BrandViewSet(viewsets.ModelViewSet):
     queryset = Brand.objects.prefetch_related('manufacture', 'manufacture__owner')
     serializer_class = BrandSerilizer
     http_method_names = ['get','post','retrieve','put','patch','delete']