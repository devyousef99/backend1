from django.shortcuts import render
from rest_framework.decorators import api_view
from account.models import *
from product.serializer import *
from rest_framework.response import Response
from .models import *
# Create your views here.

@api_view(['GET'])
def get_product(request):
    if request.method == 'GET':
        get_products = Product.objects.all()
        serializer = createPRODUCTSerializer(data=get_products, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)


@api_view(['GET'])
def get_cat(request):
    if request.method == 'GET':
        get_cats = Category.objects.all()
        serializer = CatSerializer(data=get_cats, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)