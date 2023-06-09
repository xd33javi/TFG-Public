from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Salas(models.Model):
    nombre=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imgsalas',null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salas_p',default='1')
    
    class Meta:
        verbose_name="Sala"
        verbose_name_plural="Salas"
    
    def __str__(self):
        return self.nombre
    
class Salas_c(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salas_c')
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE, related_name='rooms_c')
    
    class Meta:
        verbose_name="Sala_c"
        verbose_name_plural="Salas_c"
        
    def __str__(self):
        return self.sala.nombre   
    
class Mensajes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE, related_name='rooms')
    mensaje = models.TextField()
    
    class Meta:
        verbose_name="mensaje"
        verbose_name_plural="mensajes"