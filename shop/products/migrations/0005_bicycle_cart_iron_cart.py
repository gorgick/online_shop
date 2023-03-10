# Generated by Django 4.1.3 on 2022-12-10 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_cart_total_price_alter_cart_total_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicycle',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_bicycles', to='products.cart', verbose_name='Корзина'),
        ),
        migrations.AddField(
            model_name='iron',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_irons', to='products.cart', verbose_name='Корзина'),
        ),
    ]
