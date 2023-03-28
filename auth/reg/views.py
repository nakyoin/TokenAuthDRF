from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.status import *
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token


class RegistrateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['data'] = serializer.data
            user = serializer.user
            token = Token.objects.create(user=user)
            print(token)
            return Response({'user_token': token.key}, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

class LoginUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]
    def post(self, request: WSGIRequest, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return JsonResponse({
                'error': {
                    'code': 401,
                    'message': 'Authentification failed'
                }
            })

        user = serializer.validated_data
        print('abcd', user)
        if user:
            token_object, token_created = Token.objects.get_or_create(user=user)
            token = token_object if token_object else token_created

            return Response({'user token': token.key}, status=HTTP_200_OK)
        return Response({'error': {'message': 'Auth Failed'}})

class LogOutUserView(ListAPIView):
    def get(self, request: WSGIRequest, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            return JsonResponse({
                'error': {
                    'code': 401,
                    'message': 'Logout failed'
                }
            }, status=401)

        logout(request)

        return JsonResponse({
            'data': {
                'message': 'Logged out'
            }
        }, status=200)


class ProdView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdSerializer


class ProdDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProdSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

class CartView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

class CartDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

class CountryView(ListAPIView):
    queryset = CountryProd.objects.all()
    serializer_class = CountrySerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAdminUser,)

class CountryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CountryProd.objects.all()
    serializer_class = CountrySerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAdminUser,)

class PMView(ListAPIView):
    queryset = ProductManager.objects.all()
    serializer_class = ProdManSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAdminUser,)

class PMDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ProductManager.objects.all()
    serializer_class = ProdManSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAdminUser,)

class OrderView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_class = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)



