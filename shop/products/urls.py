from django.urls import path
from .views import (BaseView,
                    IronDetailView,
                    BicycleDetailView,
                    )

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('iron/<str:iron_slug>/', IronDetailView.as_view(), name='iron_detail'),
    path('bicycle/<str:bicycle_slug>/', BicycleDetailView.as_view(), name='bicycle_detail')
]