from rest_framework import serializers
from . models import POSclient,POSproduct,POSorder

class POSclientSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSclient
        fields = ['clients','clientsemail','phone_number','address','provider','owner','company','isactive']

class POSproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = POSproduct
        fields = ['id','productName','brand','coverImage','category','subCategory','descripton','order_quantity', 'available_quantity','sku','price','wholeSalePrice','discount']
        read_only_fields = ['id','approved','created_at','modified_at']

class POSorderSerializer(serializers.ModelSerializer):
    buyer = POSclientSerializer(read_only=False)

    class Meta:
        model = POSorder
        fields = ['id','order','products','buyer','seller', 'status', 'created_at']
        read_only_fields = ['order', 'buyer']

    def create(self, validated_data):
        print(validated_data)
        buyer = validated_data.pop('buyer')
        buyer_instance = POSclient.objects.get(owner=buyer['owner'])
        order = POSorder.objects.create(**validated_data)
        order.buyer = buyer_instance
        order.save()
        return order
