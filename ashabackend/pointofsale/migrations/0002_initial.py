# Generated by Django 4.0.4 on 2022-07-11 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('pointofsale', '0001_initial'),
        ('category', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='posproduct',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productdiscount', to='product.productdiscount', verbose_name='discount in %'),
        ),
        migrations.AddField(
            model_name='posproduct',
            name='subCategory',
            field=models.ManyToManyField(to='category.productsubcategory'),
        ),
        migrations.AddField(
            model_name='posorder',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pointofsale.posclient', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='posorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pointofsale.posproduct', verbose_name='product'),
        ),
        migrations.AddField(
            model_name='posorder',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Seller'),
        ),
        migrations.AddField(
            model_name='posclient',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Addeby'),
        ),
    ]
