from rest_framework import serializers
from product.serializer import ProductSerializer
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = (
            "product",
            "quantity",
        )