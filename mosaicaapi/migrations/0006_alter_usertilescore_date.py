# Generated by Django 4.1.5 on 2023-01-24 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosaicaapi', '0005_alter_usertilescore_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertilescore',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]