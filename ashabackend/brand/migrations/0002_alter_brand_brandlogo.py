# Generated by Django 4.0.4 on 2022-06-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brandlogo',
            field=models.ImageField(upload_to='uploads/brands ', verbose_name='brand'),
        ),
    ]
