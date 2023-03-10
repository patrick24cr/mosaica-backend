# Generated by Django 4.1.5 on 2023-01-24 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mosaicaapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='aspect1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aspect1', to='mosaicaapi.responseset'),
        ),
        migrations.AlterField(
            model_name='question',
            name='aspect2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aspect2', to='mosaicaapi.responseset'),
        ),
        migrations.AlterField(
            model_name='question',
            name='aspect3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aspect3', to='mosaicaapi.responseset'),
        ),
        migrations.AlterField(
            model_name='question',
            name='aspect4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aspect4', to='mosaicaapi.responseset'),
        ),
    ]
