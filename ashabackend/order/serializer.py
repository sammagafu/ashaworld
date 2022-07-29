from rest_framework import serializers
from .models import Order,OrderItems
from product.models import Product
from product.serializer import ProductSerializer
from django.contrib.auth.models import User

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItems
        fields = ['id','product','quantity','order']
        read_only_fields= ['id','created_at','order']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']
        read_only_fields = ['username','email']
        

class OrderSerializer(serializers.ModelSerializer):
    orderproducts = OrderProductSerializer(many=True, read_only=True)
    owner = UserSerializer(many=False, read_only=True)
    owner_id =serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='owner', write_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='orderproducts', write_only=True, many=True)
    class Meta:
        model = Order
        read_only_fields = ['id','owner','paid_at','created_at','orderproducts']
        fields = ['id','owner','owner_id','totalprice','orderstatus','active','promo_code','product_ids','orderproducts','slug','created_at']
        # depth=1
    
    def create(self, validated_data): 
        orderitems = validated_data.pop('orderproducts')
        owner = validated_data.pop('owner')
        order = Order.objects.create(**validated_data, owner=owner)
        for orderitem in orderitems:
            OrderItems.objects.create(product=orderitem, order=order)
        return order