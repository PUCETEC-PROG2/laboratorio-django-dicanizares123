# Generated by Django 4.2 on 2024-12-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('level', models.IntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('L', 'Lagartija'), ('F', 'Fuego'), ('E', 'Electrico'), ('T', 'Tierra'), ('A', 'Agua'), ('P', 'Planta')], max_length=30),
        ),
    ]
