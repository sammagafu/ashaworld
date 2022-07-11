# Generated by Django 4.0.4 on 2022-07-11 04:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInvertory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('lowcount', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Invertory',
                'verbose_name_plural': 'Invertories',
            },
        ),
    ]
