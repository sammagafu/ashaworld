# Generated by Django 4.0.4 on 2022-07-11 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pointofsale', '0003_remove_posclient_active_posclient_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posorder',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pointofsale.posclient', verbose_name='buyer'),
        ),
    ]
