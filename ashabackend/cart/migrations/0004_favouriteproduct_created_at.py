# Generated by Django 4.0.4 on 2022-06-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_favouriteproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='favouriteproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
