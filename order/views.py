from datetime import timezone
from itertools import product
from rest_framework import status
from typing import OrderedDict
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from account.models import *
from order.serializer import OrdrItemSerializer
from product.serializer import *
from rest_framework.response import Response
from .models import *
from product.serializer import createPRODUCTSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@api_view(['GET'])
def get_cart_usr(request,pk):
    if request.method == 'GET':
        user_profile = get_object_or_404(Profile, user=pk)
        order = Order.objects.filter(owner=user_profile, is_ordered=False).first()
        if order is None:
            Order.objects.create(owner=user_profile, is_ordered=False)
        order_item =OrderItem.objects.filter(refrence_id=order.id)
        serializer = OrdrItemSerializer(data=order_item, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data)

@csrf_exempt
def add_to_cart(request, pk):
    item = get_object_or_404(Product, id=pk)
    print(item)
    order = Order.objects.filter(owner=request.user.profile, is_ordered=False).first()
    print(order)
    order_item = OrderItem.objects.filter(
        product=item,
        refrence_id=order.id
    )
    print(order_item)
    serializer = OrdrItemSerializer(data=order_item)
    serializer.is_valid(raise_exception=False)
    print(order_item)
    if order_item.exists():
        order_item.quantity +=1
        order_item.save()
        return Response(serializer.data)
    else:
        order_item.add(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
