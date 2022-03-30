from rest_framework import serializers
from .models import *


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('__all__')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ('__all__')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create_set(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.usr_img = validated_data.get('usr_img', instance.usr_img)
        instance.save()
        return instance
