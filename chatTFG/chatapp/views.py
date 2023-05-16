from django.shortcuts import render,HttpResponse

# Create your views here.

from .models import Salas

def home(request):
    
    salas_v = Salas.objects.all()
    
    return render(request,'chatapp/home.html',{'salas_p':salas_v})

def room(request, room_name):
    return render(request, "chatapp/room.html", {"room_name": room_name})