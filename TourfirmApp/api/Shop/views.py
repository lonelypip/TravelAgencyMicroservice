from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, JsonResponse 
from TourfirmApp.models import (
    Country,
    Order
)


from .serializers import (
    CountryListSerializer,
    CountryDetailSerializer,
    OrderCreateSerializer
)


from .pagination import ProductLimitOffsetPagination, ProductPageNumberPagination



from rest_framework.views import APIView

from rest_framework.generics import (
   ListAPIView, 
   RetrieveAPIView, 
   UpdateAPIView, 
   DestroyAPIView, 
   CreateAPIView,
   RetrieveUpdateAPIView
)

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)



class CountryListAPIView(ListAPIView): 
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer

    #def get_queryset()


class CountryDetailAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    lookup_field = 'slug'


# class UserUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserUpdateSerializer
#     lookup_field = 'id'
   


# class CategoryDeleteAPIView(DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryDetailSerializer
#     lookup_field = 'slug'


# class CategoryCreateAPIView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryCreateSerializer


# class ProductCreateAPIView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductCreateSerializer

# class ProductDetailAPIView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer
#     lookup_field = 'slug'
    

# class ProductListAPIView(ListAPIView): 
#     queryset = Product.objects.all()
#     serializer_class = ProductListSerializer
#     pagination_class = ProductPageNumberPagination

#     #def get_queryset()


# class ProductUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductUpdateSerializer
#     lookup_field = 'slug'


# class ProductDeleteAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerializer
#     lookup_field = 'slug'

# class CartItemCreateAPIView(CreateAPIView):
#     queryset = CartItem.objects.all()
#     serializer_class = CartItemCreateSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer