from django.urls import path
from .views import UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView, UserCreateAPIView
from rest_framework.authtoken import views
urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='api_user_create_url'),
    path('', UserListAPIView.as_view(), name='api_user_list_url'),
    path('<int:id>/', UserDetailAPIView.as_view(), name='api_user_detail_url'),
    path('<int:id>/update/', UserUpdateAPIView.as_view(), name='api_user_update_url'),
    path('<int:id>/delete/', UserDeleteAPIView.as_view(), name='api_user_delete_url'),
    path('token-auth/', views.obtain_auth_token, name='api_token_auth_url'),
]
