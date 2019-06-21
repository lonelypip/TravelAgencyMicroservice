from rest_framework import serializers
from rest_framework.serializers import ( 
    ModelSerializer, 
    HyperlinkedIdentityField, 
    SerializerMethodField
)

from TourfirmApp.models import (
    Country,
    Order
)


# class CategoryCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('name','slug')

# class CategoryDetailSerializer(serializers.ModelSerializer):
#    class Meta:
#       model = Category
#       fields = ('id','name','slug')

# class CategoryChildSerializer(serializers.ModelSerializer):
#     class Meta:
#       model = Product
#       fields = ('id','category','title','slug','description', 'price')


# class CategoryListSerializer(serializers.ModelSerializer):
#     # url = HyperlinkedIdentityField(
#     #     view_name='api_user_detail_url',
#     #     lookup_field='id'
#     # )

#     # products = SerializerMethodField()
#     class Meta:
#         model = Category
#         fields = ('id','name','slug','products')
    
#     # def get_products(self, obj):
#     #     return CategoryChildSerializer(obj)


# class CategoryUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id','name')

# class ProductCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('category','title','slug','description', 'price')

class CountryDetailSerializer(serializers.ModelSerializer):
    background_image = SerializerMethodField()
    image_1 = SerializerMethodField()
    image_2 = SerializerMethodField()
    image_3 = SerializerMethodField()
    image_4 = SerializerMethodField()
    class Meta:
        model = Country
        fields = (
            'name', 
            'description', 
            'price',
            'sities',
            'slug',
            'background_image',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
        )
    def get_background_image(self, obj):
        try:
            background_image = obj.background_image.url
        except:
            background_image = None
        return background_image

    def get_image_1(self, obj):
        try:
            image_1 = obj.image_1.url
        except:
            image_1 = None
        return image_1

    def get_image_2(self, obj):
        try:
            image_2 = obj.image_2.url
        except:
            image_2 = None
        return image_2
    
    def get_image_3(self, obj):
        try:
            image_3 = obj.image_3.url
        except:
            image_3 = None
        return image_3
    
    def get_image_4(self, obj):
        try:
            image_4 = obj.image_4.url
        except:
            image_4 = None
        return image_4

class CountryListSerializer(serializers.ModelSerializer):
    main_image = SerializerMethodField()
    get_absolute_url = SerializerMethodField()
    class Meta:
        model = Country
        fields = (
            'name', 
            'description', 
            'price', 
            'main_image',
            'sities',
            'get_absolute_url',
            'slug'
        )
    def get_get_absolute_url(self, obj):
        return obj.get_absolute_url()
    def get_main_image(self, obj):
        try:
            main_image = obj.main_image.url
        except:
            main_image = None
        return main_image


# class ProductUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('title','slug','description', 'price')


# class CartItemCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ('product','qty','item_total')


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'items', 
            'total', 
            'first_name', 
            'last_name',
            'phone',
            'address',
            'buying_type',
            'comment'
        )
