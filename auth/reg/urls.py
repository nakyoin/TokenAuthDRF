from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('register/', RegistrateUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogOutUserView.as_view(), name='logout'),
    path('order/', OrderView.as_view(), name='order'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
    path('country/', CountryView.as_view(), name='country'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country'),
    path('products/', ProdView.as_view(), name='products'),
    path('products/<int:pk>/', ProdDetailView.as_view(), name='products'),
    path('prodman/', PMView.as_view(), name='prodman'),
    path('prodman/<int:pk>/', PMDetailView.as_view(), name='prodmandeatil'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:pk>', CartDetailView.as_view(), name='cartdetail'),
]
