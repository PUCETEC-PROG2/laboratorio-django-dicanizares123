# Generated by Django 4.2 on 2025-01-15 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('B', 'Fuego'), ('E', 'Electrico'), ('C', 'Tierra'), ('A', 'Agua'), ('F', 'Lagartija'), ('D', 'Planta')], max_length=30),
        ),
    ]
