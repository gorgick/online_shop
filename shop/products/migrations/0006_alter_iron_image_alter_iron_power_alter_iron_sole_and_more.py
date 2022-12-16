# Generated by Django 4.1.3 on 2022-12-10 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_bicycle_cart_iron_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iron',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/products'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='power',
            field=models.IntegerField(blank=True, null=True, verbose_name='Мощность'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='sole',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Материал подошвы'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='type',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Вид утюга'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='volume',
            field=models.IntegerField(blank=True, null=True, verbose_name='Обьем резервуара для воды'),
        ),
    ]