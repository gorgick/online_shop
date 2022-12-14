from django.urls import path
from .views import (BaseView,
                    IronDetailView,
                    BicycleDetailView,
                    CartView,
                    AddToCartView,
                    DeleteFromCartView,
                    )

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('delete-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('iron/<str:slug>/', IronDetailView.as_view(), name='iron_detail'),
    path('bicycle/<str:slug>/', BicycleDetailView.as_view(), name='bicycle_detail'),
    path('cart/', CartView.as_view(), name='cart'),
]