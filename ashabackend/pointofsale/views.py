from rest_framework import generics
from . models import ShippingAddress

class ShippingListAPI(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.data.get("product", None))
        serializer.save(owner=self.request.user)
