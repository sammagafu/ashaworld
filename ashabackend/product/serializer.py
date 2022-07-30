from typing_extensions import Required
from rest_framework import serializers

from brand.models import Brand
from brand.serializer import BrandSerilizer
from .models import Product,ProductImage
from category.serializer import CategorSerializer
from category.models import ProuctCategory

class ProudctImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['get_images',]

class ProductSerializer(serializers.ModelSerializer):
    brand_qs = Brand.objects.prefetch_related('manufacture', 'manufacture__owner')
    category_qs = ProuctCategory.objects.all()
    brand = BrandSerilizer(brand_qs, read_only=True)
    # images =  ProudctImageSerializer(write_only=True,many=True)
    category = CategorSerializer(category_qs,read_only=True)
    brand_id =serializers.PrimaryKeyRelatedField(queryset=brand_qs, source='brand', write_only=True, required=False)
    images_id =serializers.PrimaryKeyRelatedField(source='images', read_only=True, many=True)
    category_id =serializers.PrimaryKeyRelatedField(queryset=category_qs,source='category', write_only=True, required=False)

    class Meta:
        model =  Product
        read_only_fields = ["images_id"]
        fields = [
            "id","slug",
            "productName","get_coverImage",
            "price","wholeSalePrice",
            "brand","category",
            "descripton","sku",
             'brand_id',"images_id",
             "coverImage", 'category_id'
        ]
    
    def create(self, validated_data):
        print("Initial data ==>",self.initial_data)
        print("Validated data ==>",validated_data)
        try:
            brand = validated_data.pop('brand')
        except:
            brand_data = self.initial_data.pop('brand.brandName')
            brand = Brand.objects.create(brandName=brand_data[0])
        try:
            category= validated_data.pop('category')
        except:
            category_data = self.initial_data.pop('category.categoryname')
            category = ProuctCategory.objects.create(categoryname=category_data[0])
        # images_data = validated_data.pop('images')
        product = Product.objects.create(**validated_data)
        product.category = category
        product.brand = brand
        product.save()
        return product
