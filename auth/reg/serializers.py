from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *

class UserRegistrateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: 'Пароль не совпадает'})
        user.set_password(password)
        user.save()


        self.user = user

        return self.user


class UserLoginSerializer(serializers.Serializer):
    user: User = None
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user:
            return user
        return False

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProdManSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManager
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'