# Generated by Django 4.1.5 on 2023-01-27 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosaicaapi', '0011_alter_usertilescore_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertilescore',
            name='date',
            field=models.DateTimeField(blank=True, default='2023-01-27 02:48:35', null=True),
        ),
    ]
