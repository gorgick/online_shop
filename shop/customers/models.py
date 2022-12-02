from Tools.demo.mcast import sender
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, verbose_name='Никнейм', null=True, blank=True)
    email = models.EmailField(max_length=200, verbose_name='Почта', null=True, blank=True)
    user_image = models.ImageField(upload_to='img/customers', null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)


def create_customer(sender, instance, created, **kwargs):
    if created:
        user = instance
        user = Customer.objects.create(
            user=user,
            username=instance.username,
            email=instance.email,
        )


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_customer, sender=User)
post_delete.connect(delete_user, sender=Customer)
