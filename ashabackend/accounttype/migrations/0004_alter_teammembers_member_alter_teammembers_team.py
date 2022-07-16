# Generated by Django 4.0.4 on 2022-07-15 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounttype', '0003_teammembers_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teammember', to='accounttype.team'),
        ),
    ]
