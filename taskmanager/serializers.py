from rest_framework import serializers
from .models import Card,Column,Desk
from django.db import models
from django.contrib.auth.models import User



class DeskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Desk
        fields = ('id','title','user','type',)

class DeskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Desk
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username',instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = '__all__'