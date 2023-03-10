from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginView, RegisterView

urlpatterns =[
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]