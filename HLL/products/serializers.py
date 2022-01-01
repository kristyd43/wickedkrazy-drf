from rest_framework import serializers
from .models import Product, cartItem

class ProductSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()
    image = serializers.URLField()
    cart = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class cartItemSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    cart_quantity = serializers.IntegerField()
    cartUser = serializers.CharField(max_length=200)
    product_id = serializers.IntegerField()

    def create(self, validated_data):
        return cartItem.objects.create(**validated_data)
