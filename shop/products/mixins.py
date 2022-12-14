from django.views.generic.detail import SingleObjectMixin

from customers.models import Customer
from products.models import Cart


class CartMixin(SingleObjectMixin):

    def dispatch(self, request, *args, **kwargs):
        customer = Customer.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(owner=customer).first()
        if not cart:
            cart = Cart.objects.create(owner=customer)
        self.cart = cart
        return super(CartMixin, self).dispatch(request, *args, **kwargs)

