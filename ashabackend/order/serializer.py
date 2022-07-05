from time import clock_getres
from rest_framework import serializers
from .models import Order,OrderItems
from product.serializer import ProductSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItems
        fields = ['product','quantity','order']
        read_only_fields = ['id','created_at']

class OrderSerializer(serializers.ModelSerializer):
    orderproducts = OrderProductSerializer(many=True)
    class Meta:

        model = Order
        read_only_fields = ('owner','paid_at','slug','created_at')
        fields = ['totalprice','orderstatus','active','promo_code','orderproducts']
        
    
    def create(self, validated_data):
        orderitems = validated_data.pop('orderproducts')
        print(orderitems)
        order = Order.objects.create(**validated_data)
        for orderitems in orderitems:
            orderitems.objects.create(order=order, **orderitems)
        return order