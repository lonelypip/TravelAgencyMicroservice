from django.urls import path, include
from .views import (
    CountryListAPIView,
    CountryDetailAPIView,
    OrderCreateAPIView
)



urlpatterns = [
    # path('category/create/', CategoryCreateAPIView.as_view(), name='api_category_create_url'),
    # path('category/', CategoryListAPIView.as_view(), name='api_category_list_url'),
    # path('category/<str:slug>/', CategoryDetailAPIView.as_view(), name='api_category_detail_url'),
    # # path('users/<int:id>/update/', UserUpdateAPIView.as_view(), name='api_user_update_url'),
    # path('category/<str:slug>/delete/', CategoryDeleteAPIView.as_view(), name='api_category_delete_url'),
    # path('token-auth/', views.obtain_auth_token, name='api_token_auth_url')
    # path('product/create/', ProductCreateAPIView.as_view(), name='api_product_create_url'),
    # path('product/<str:slug>/', ProductDetailAPIView.as_view(), name='api_product_detail_url'),
    # path('product/', ProductListAPIView.as_view(), name='api_product_list_url'),
    # path('product/<str:slug>/update/', ProductUpdateAPIView.as_view(), name='api_product_update_url'),
    # path('product/<str:slug>/delete/', ProductDeleteAPIView.as_view(), name='api_product_delete_url'),
    # path('cart-item/create/', CartItemCreateAPIView.as_view(), name='api_cart_item_create_url'),
    path('shop/country/', CountryListAPIView.as_view(), name='api_country_list_url'),
    path('shop/country/<str:slug>/', CountryDetailAPIView.as_view(), name='api_country_detail_url'),
    path('shop/order/create/', OrderCreateAPIView.as_view(), name='api_order_create_url'),
    path('users/', include('TourfirmApp.api.Users.urls'))
]
