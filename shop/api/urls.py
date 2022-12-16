from django.urls import path
from .views import get_bicycles, get_carts, get_cart
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('bicycles/', get_bicycles),
    path('carts/', get_carts),
    path('carts/<int:pk>/', get_cart),
]
