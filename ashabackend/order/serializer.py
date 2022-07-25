from rest_framework import serializers
from .models import Order,OrderItems
from django.conf import settings
from product.serializer import ProductSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItems
        fields = ['product','quantity','order']
        read_only = ('id','created_at')

class OrderSerializer(serializers.ModelSerializer):
    orderproducts = OrderProductSerializer(many=True)
    # owner = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = Order
        depth=1
        read_only = ('owner','paid_at','created_at')
        fields = ['id','owner','totalprice','orderstatus','active','promo_code','orderproducts','slug','created_at']
    
    def create(self, validated_data):
        orderitems = validated_data.pop('orderproducts')
        print(orderitems)
        order = Order.objects.create(**validated_data)
        for orderitems in orderitems:
            orderitems.objects.create(order=order, **orderitems)
        return order