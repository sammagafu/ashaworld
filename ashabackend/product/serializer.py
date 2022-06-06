from rest_framework import serializers
from .models import Product,ProductImage
from category.serializer import CategorSerializer

class ProudctImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['images',]

class ProductSerializer(serializers.ModelSerializer):
    images =  ProudctImageSerializer(many=True)
    category = CategorSerializer(read_only=True)
    class Meta:
        model =  Product
        fields = (
            "id",
            "slug",
            "productName",
            "coverImage",
            "price",
            "wholeSalePrice",
            "brand",
            "category",
            "descripton",
            "sku",
            "images",
            "get_absolute_url"
            )
