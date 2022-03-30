from rest_framework import serializers
from .models import *

# from account.serializer import StoreSerializer, UserSerializer

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['cat_name', 'id']


class SIZESerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('sz_name')


# class COLORSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Color
#         fields = ('color_name')


class VariantSerializer(serializers.ModelSerializer):
    size = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProductDetail
        fields = ['pr_price', 'in_stock', 'pr_size', 'size', 'pr_qunatity', 'pr_type', 'pr_img']


class createPRODUCTSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    owner = serializers.StringRelatedField(read_only=True)
    detail = VariantSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id' , 'owner', 'pr_name', 'pr_description', 'category', 'create_at', 'update_at', 'detail']


class ProductName(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pr_name', 'id']
