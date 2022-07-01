from rest_framework import serializers
from product.serializer import ProductSerializer
from .models import Cart,FavouriteProduct

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        # read_only_fields = ['get_total_price']
        fields = ["id","product","quantity","get_total_price"]


class FavouriteProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = FavouriteProduct
        fields = ["product"]

