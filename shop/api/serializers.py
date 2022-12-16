from rest_framework import serializers
from products.models import Bicycle, Cart
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class BicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicycle
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    owner = CustomerSerializer(many=False)
    bicycles = BicycleSerializer(many=True)

    class Meta:
        model = Cart
        fields = "__all__"
