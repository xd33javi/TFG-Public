from django.contrib import admin

from .models import Salas,Mensajes,Salas_c

admin.site.register(Salas)
admin.site.register(Salas_c)
admin.site.register(Mensajes)