from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse


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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bicycle_detail', kwargs={'bicycle_slug': self.slug})

    class Meta:
        verbose_name = "Велосипед"
        verbose_name_plural = "Велосипеды"


class Iron(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название утюга')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    type = models.CharField(max_length=200, verbose_name='Вид утюга')
    sole = models.CharField(max_length=200, verbose_name='Материал подошвы')
    volume = models.IntegerField(verbose_name='Обьем резервуара для воды')
    power = models.IntegerField(verbose_name='Мощность')
    more = models.TextField(verbose_name='В комплекте', blank=True, null=True)
    image = models.ImageField(upload_to='img/products', null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    stock = models.IntegerField(default=1, verbose_name='Имеется в наличии')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('iron_detail', kwargs={'iron_slug': self.slug})

    class Meta:
        verbose_name = "Утюг"
        verbose_name_plural = "Утюги"
