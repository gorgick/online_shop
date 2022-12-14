from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .utils import recalc_cart

from .mixins import CartMixin
from .models import *


class BaseView(View):
    def get(self, request, *args, **kwargs):
        irons = Iron.objects.all()
        products = get_products_for_main_page('iron', 'bicycle')
        return render(request, 'products/main_page.html', {'irons': irons, 'products': products})


class IronDetailView(DetailView):
    model = Iron
    slug_url_kwarg = 'slug'
    template_name = 'products/iron_detail.html'
    context_object_name = 'iron'


class BicycleDetailView(DetailView):
    model = Bicycle
    slug_url_kwarg = 'slug'
    template_name = 'products/bicycle_detail.html'
    context_object_name = 'bicycle'


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'products/cart.html', {'cart': self.cart})


class AddToCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        cat_slug = kwargs.get('ct_model')
        if cat_slug == 'iron':
            iron = Iron.objects.get(slug=kwargs.get('slug'))
            self.cart.irons.add(iron)
            recalc_cart(self.cart)
        if cat_slug == 'bicycle':
            bicycle = Bicycle.objects.get(slug=kwargs.get('slug'))
            self.cart.bicycles.add(bicycle)
            recalc_cart(self.cart)
        return HttpResponseRedirect('/')


class DeleteFromCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        cat_slug = kwargs.get('ct_model')
        if cat_slug == 'iron':
            iron = Iron.objects.get(slug=kwargs.get('slug'))
            self.cart.irons.remove(iron)
        if cat_slug == 'bicycle':
            bicycle = Bicycle.objects.get(slug=kwargs.get('slug'))
            self.cart.bicycles.remove(bicycle)
        recalc_cart(self.cart)
        return HttpResponseRedirect('/')




