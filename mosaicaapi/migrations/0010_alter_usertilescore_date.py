# Generated by Django 4.1.5 on 2023-01-27 01:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mosaicaapi', '0009_alter_usertilescore_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertilescore',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
