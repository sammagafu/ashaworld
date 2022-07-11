from dataclasses import field
from rest_framework import serializers
from . models import ShippingAddress

class ShippingDetails(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        field = '__all__'