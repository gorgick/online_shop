from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import *


class BaseView(View):
    def get(self, request, *args, **kwargs):
        irons = Iron.objects.all()
        products = get_products_for_main_page('iron', 'bicycle')
        return render(request, 'products/main_page.html', {'irons': irons, 'products': products})


class IronDetailView(DetailView):
    model = Iron
    slug_url_kwarg = 'iron_slug'
    template_name = 'products/iron_detail.html'
    context_object_name = 'iron'


class BicycleDetailView(DetailView):
    model = Bicycle
    slug_url_kwarg = 'bicycle_slug'
    template_name = 'products/bicycle_detail.html'
    context_object_name = 'bicycle'
