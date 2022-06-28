from rest_framework import serializers
from . models import Brand

class BrandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brandName','get_brandImg']