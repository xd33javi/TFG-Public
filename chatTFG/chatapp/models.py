from django.db import models

# Create your models here.
class Salas(models.Model):
    nombre=models.CharField(max_length=50)
    
    class Meta:
        verbose_name="Sala"
        verbose_name_plural="Salas"
    
    def __str__(self):
        return self.nombre
    