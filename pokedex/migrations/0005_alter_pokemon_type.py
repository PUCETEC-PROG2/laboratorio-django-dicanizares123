# Generated by Django 4.2 on 2025-01-20 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_trainer_picture_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('C', 'Tierra'), ('A', 'Agua'), ('D', 'Planta'), ('B', 'Fuego'), ('E', 'Electrico'), ('F', 'Lagartija')], max_length=30),
        ),
    ]
