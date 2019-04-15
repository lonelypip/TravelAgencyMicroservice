from django.urls import path
from .views import *

urlpatterns = [
   path('', home, name='home_url'),
   path('country/<str:slug>/', CountryDetail.as_view(), name="country_detail_url"),
   path('tours/', ToursList.as_view(), name="tours_list_url"),
   path('cart/', cart_view, name="cart_url"),
   path('add-to-cart/', add_to_cart_view, name="add_to_cart_url"),
   path('remove-from-cart/', remove_from_cart_view, name="remove_from_cart_url"),
   path('change-item-qty/', change_item_qty, name="change_item_qty_url"),
   path('checkout/', checkout_view, name="checkout_url"),
   path('order/', order_create_view, name="create_order_url"),
]