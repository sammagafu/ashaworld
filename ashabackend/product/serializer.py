from rest_framework import serializers

from brand.serializer import BrandSerilizer
from .models import Product,ProductImage
from category.serializer import CategorSerializer

class ProudctImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['get_images',]

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerilizer()
    images =  ProudctImageSerializer(many=True)
    category = CategorSerializer(read_only=True)
    class Meta:
        model =  Product
        fields = [
            "id",
            "slug",
            "productName",
            "get_coverImage",
            "price",
            "wholeSalePrice",
            "brand",
            "category",
            "descripton",
            "sku",
            "images",
            "get_absolute_url"
        ]
