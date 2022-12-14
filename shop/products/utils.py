from django.db import models


def recalc_cart(cart):
    cart_data = cart.irons.aggregate(models.Sum('price'), models.Count('id'))
    cart_data_b = cart.bicycles.aggregate(models.Sum('price'), models.Count('id'))
    total_price = 0
    total_products = 0
    if cart_data.get('price__sum'):
        total_price += cart_data['price__sum']
    total_products += cart_data['id__count']
    if cart_data_b.get('price__sum'):
        total_price += cart_data_b['price__sum']
    total_products += cart_data_b['id__count']
    cart.total_price = total_price
    cart.total_product = total_products
    cart.save()