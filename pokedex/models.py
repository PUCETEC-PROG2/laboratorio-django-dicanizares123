from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null= False)
    last_name = models.CharField(max_length=30, null= False)
    birth_date = models.DateField()
    level = models.IntegerField(default=1)
    picture = models.ImageField(upload_to="trainer_images", null=True)
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}' 
    
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def clean(self):
        if self.birth_date > date.today():
            raise ValidationError('La fecha de nacimiento no puede ser en el futuro.')


# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=40, null= False)
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('B', 'Fuego'),
        ('C', 'Tierra'),
        ('D', 'Planta'),
        ('E', 'Electrico'),
        ('F', 'Lagartija'),
    }
    type = models.CharField(max_length= 30, choices= POKEMON_TYPES, null= False)
    weigth = models.DecimalField(max_digits=4,decimal_places=2)
    heigth = models.DecimalField(max_digits=5,decimal_places=3)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to="pokemon_images")
    
    def __str__(self):
        return self.name
    

    
    
