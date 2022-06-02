from rest_framework import serializers
from .models import Product,ProductImage

class ProudctImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['images',]

class ProductSerializer(serializers.ModelSerializer):
    images =  ProudctImageSerializer(many=True)
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
            "subCategory",
            "descripton",
            "sku",
            "images"
            )
