from rest_framework import serializers
from .models import Order,OrderItems
from product.models import Product
from product.serializer import ProductSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(read_only=True)
    product = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = OrderItems
        fields = ['product','quantity','order']
        read_only = ('id','created_at')

class OrderSerializer(serializers.ModelSerializer):
    # orderproducts = OrderProductSerializer(many=True)
    orderproducts = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    # owner = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Order
        read_only = ('owner','paid_at','created_at', 'id')
        fields = ['owner','totalprice','orderstatus', 'id','active','promo_code','orderproducts','slug','created_at']
        depth = 1
    
    def create(self, validated_data):
        orderitems = validated_data.pop('orderproducts')
        print(orderitems)
        order = Order.objects.create(**validated_data)
        for orderitem in orderitems:
            OrderItems.objects.create(product=orderitem, order=order)
        return order