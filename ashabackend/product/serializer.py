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
    brand = BrandSerilizer(Brand.objects.prefetch_related('manufacture'))
    # images =  ProudctImageSerializer(write_only=True,many=True)
    category = CategorSerializer()
    brand_id =serializers.PrimaryKeyRelatedField(source='brand', read_only=True)
    images_id =serializers.PrimaryKeyRelatedField(source='images', read_only=True, many=True)

    class Meta:
        model =  Product
        read_only_fields = [ 'brand_id', "images_id"]
        fields = [
            "id","slug",
            "productName","get_coverImage",
            "price","wholeSalePrice",
            "brand","category",
            "descripton","sku",
             'brand_id',"images_id"
        ]
    
    def create(self, validated_data):
        print("Initial data ==>",self.initial_data)
        print("Validated data ==>",validated_data)
        brand_data = validated_data.pop('brand')
        category_data = validated_data.pop('category')
        # images_data = validated_data.pop('images')
        # company_instance = POSclient.objects.get(owner=buyer['owner'])
        category = ProuctCategory.objects.create(**category_data)
        product = Product.objects.create(**validated_data)
        product.category = category
        # product.brand = buyer_instance
        product.save()
        return product
