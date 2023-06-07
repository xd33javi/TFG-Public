from django import forms
from .models import Salas

class formularioCrearSala(forms.ModelForm):
    class Meta:
        model = Salas
        fields = ['nombre','imagen',]
        
   