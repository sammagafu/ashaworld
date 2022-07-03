from rest_framework import serializers
from .models import Order,OrderItems

class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItems
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['slug','assigned_to','created_at']

    def create(self, validated_data):
        order_product = validated_data.pop('order')
        order = Order.objects.create(**order_product)
        for order_product in order_product:
            OrderItems.objects.create(order=order, **order_product)
        return order