from rest_framework import serializers
from . models import POSclient,POSproduct,POSorder

class POSclientSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSclient
        fields = 'clients','clientsemail','phone_number','address','provider','owner','company','isactive'

class POSproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSproduct
        fields = ['id','productName','brand','coverImage','category','subCategory','descripton','order_quantity', 'available_quantity','sku','price','wholeSalePrice','discount']
        read_only_fields = ['id','approved','created_at','modified_at']

class POSorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSorder
        fields = ['products','buyer','seller']
        read_only_fields = ['order']

    def perform_create(self, serializer):
        print(dir(self.request))
        serializer.save()
