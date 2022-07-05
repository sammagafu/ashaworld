from itertools import product
from rest_framework import serializers
from .models import Order,OrderItems

class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = ['product','quantity']
        read_only_fields = ['id','order','created_at']

class OrderSerializer(serializers.ModelSerializer):
    product = OrderProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ['product','totalprice','orderstatus','active','promo_code']
        read_only_fields = ['owner','paid_at','slug','created_at']

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        order = Order.objects.create(**validated_data)
        for productdata in product_data:
            OrderItems.objects.create(order=order, **productdata)
        return order