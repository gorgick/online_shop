from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from customers.models import Customer


def get_products_for_main_page(*args, **kwargs):
    ct_models = ContentType.objects.filter(model__in=args)
    products = []
    for ct_model in ct_models:
        model_products = ct_model.model_class().objects.all()
        products.extend(model_products)
    return products


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Bicycle(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название велосипеда')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    kind = models.CharField(max_length=200, verbose_name='Класс велосипеда')
    wheels = models.IntegerField(verbose_name='Диаметр колес')
    growth = models.CharField(max_length=200, verbose_name='Рост')
    front_brake_type = models.CharField(max_length=200, verbose_name='Тип переднего тормоза', null=True)
    rear_brake_type = models.CharField(max_length=200, verbose_name='Тип заднего тормоза', null=True)
    material = models.CharField(max_length=100, verbose_name='Материал рамы')
    image = models.ImageField(upload_to='img/products', null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    stock = models.IntegerField(default=1, verbose_name='Имеется в наличии')
    slug = models.SlugField(unique=True)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', null=True, on_delete=models.CASCADE,
                             related_name='related_bicycles')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bicycle_detail', kwargs={'slug': self.slug})

    @property
    def ct_model(self):
        return self._meta.model_name

    class Meta:
        verbose_name = "Велосипед"
        verbose_name_plural = "Велосипеды"


class Iron(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название утюга')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    type = models.CharField(max_length=200, verbose_name='Вид утюга', null=True, blank=True)
    sole = models.CharField(max_length=200, verbose_name='Материал подошвы', null=True, blank=True)
    volume = models.IntegerField(verbose_name='Обьем резервуара для воды', null=True, blank=True)
    power = models.IntegerField(verbose_name='Мощность', null=True, blank=True)
    more = models.TextField(verbose_name='В комплекте', blank=True, null=True)
    image = models.ImageField(upload_to='img/products', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    stock = models.IntegerField(default=1, verbose_name='Имеется в наличии')
    slug = models.SlugField(unique=True)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', null=True, on_delete=models.CASCADE,
                             related_name='related_irons')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('iron_detail', kwargs={'slug': self.slug})

    @property
    def ct_model(self):
        return self._meta.model_name

    class Meta:
        verbose_name = "Утюг"
        verbose_name_plural = "Утюги"


class Cart(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Покупатель')
    total_product = models.PositiveIntegerField(default=1, verbose_name='Кол-во товара')
    total_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Полная стоимость', default=0)
    in_order = models.BooleanField(default=False)
    bicycles = models.ManyToManyField(Bicycle, blank=True, related_name='related_cart',
                                      verbose_name='Велосипеды для корзины')
    irons = models.ManyToManyField(Iron, blank=True, related_name='related_cart',
                                   verbose_name='Утюги для корзины')

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
