# Generated by Django 4.0.4 on 2022-07-03 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='paid_at',
            field=models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Payment Date'),
        ),
        migrations.AddField(
            model_name='order',
            name='promo_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderstatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded'), ('Disputed', 'Disputed'), ('Shipped', 'Shipped'), ('Paid', 'Paid'), ('Deliverd', 'Delivered')], default='Pending', max_length=50),
        ),
    ]