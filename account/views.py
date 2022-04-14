from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework.authtoken.models import Token
from .serializer import *
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register_view(request):
    if request.method=='POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors)

# class TestLoginAppView(ObtainAuthToken):
#     def get(self, request):
#         sz = UserSerializer(data=request.data)
#         user = Profile.objects.filter(username=request.data, password=request.data).all()
#         sz.is_valid()
#         if user.exists():
#             return Response(sz.data)
#         return Response(sz.errors)

@api_view(['GET'])
def get(request):
    sz = UserSerializer(data=request.data)
    user = Usr.objects.filter(username=request.data, password=request.data).all()
    sz.is_valid()
    if user.exists():
        return Response(sz.data)
    return Response(sz.data)


@api_view(['GET'])
def get_all_user(request):
    if request.method == 'GET':
        get_user = Profile.objects.all()
        serializer = UserSerializer(data=get_user, many=True)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
def user_profile(request, pk):
    if request.method == 'GET':
        usr_profile = Profile.objects.get(pk=pk)
        serializer = UserSerializer(data=usr_profile)
        serializer.is_valid(raise_exception=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)