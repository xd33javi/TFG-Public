from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Salas

@login_required(login_url='/accounts/login/?next=/chat/')
def home(request):
    
    salas_v = Salas.objects.all()
        
    return render(request,'chatapp/home.html',{'salas_p':salas_v})


@login_required(login_url='/accounts/login/?next=/chat/')
def room(request, room_name):
    return render(request, "chatapp/room.html", {"room_name": room_name})