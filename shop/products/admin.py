from django.contrib import admin
from .models import (
    Category,
    Bicycle,
    Iron,
    Cart
)

admin.site.register(Category)
admin.site.register(Bicycle)
admin.site.register(Iron)
admin.site.register(Cart)