from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .models import Mensajes,Salas
# Create your views here.

from .models import Salas

@login_required(login_url='/accounts/login/?next=/chat/')
def home(request,room_name=""):
    
    if room_name=="":
    
        salas_v = Salas.objects.all()
            
        return render(request,'chatapp/home.html',{'salas_p':salas_v})
    else:
        salas_v = Salas.objects.all()
        sala_obj=Salas.objects.get(id=room_name)
        mensajes= Mensajes.objects.filter(sala=sala_obj)
          
        return render(request,'chatapp/home.html',{'salas_p':salas_v,"room_name": room_name,'old_msg':mensajes})
        

"""
@login_required(login_url='/accounts/login/?next=/chat/')
def room(request, room_name):
    sala_obj=Salas.objects.get(id=room_name)
    mensajes= Mensajes.objects.filter(sala=sala_obj)
    return render(request, "chatapp/room.html", {"room_name": room_name,'old_msg':mensajes})
"""