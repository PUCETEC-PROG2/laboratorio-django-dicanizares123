from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'weigth': 'Peso',
            'Heigth': 'Altura',
            'trainer': 'Entrenador',
            'picture': 'Imágen'
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'weigth': forms.NumberInput(attrs={'class': 'form-control'}),
            'Heigth': forms.NumberInput(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'})
            
            
        }
    
