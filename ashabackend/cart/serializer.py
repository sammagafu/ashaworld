from rest_framework import serializers
from product.serializer import ProductSerializer
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = (
            "product",
            "quantity",
            
        )
        read_only_fields = ("get_total_price")