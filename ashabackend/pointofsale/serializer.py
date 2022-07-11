from rest_framework import serializers
from . models import POSclient,POSproduct,POSorder

class POSclientSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSclient
        fields = 'clients','clientsemail','phone_number','address','provider','owner','company','isactive'

class POSproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSproduct
        fields = ['brand','coverImage','category','subCategory','descripton','sku','price','wholeSalePrice','discount']
        read_only = ['approved','created_at','modified_at']

class POSorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSorder
        fields = ['product','buyer','seller']
        read_only = ['order']