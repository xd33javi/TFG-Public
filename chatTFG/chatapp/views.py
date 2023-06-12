from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .models import Mensajes,Salas,Salas_c
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import formularioCrearSala
# Create your views here.

from .models import Salas

def welcome(request):
    if request.user.is_authenticated:
        return redirect(to="/chat")
    else:
        return render(request,'chatapp/welcome.html')

def register(request):
    
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST['username']
            password=request.POST['password1']
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='index')
        else:
            return render(request,"registration/registration.html",{"form":form})

    else:
        form=UserCreationForm() 
        return render(request,"registration/registration.html",{"form":form})

@login_required(login_url='/accounts/login/?next=/chat/')
def home(request,room_name=""):
    
    if room_name=="":
    
        salas_c = request.user.salas_c.all()
            
        return render(request,'chatapp/home.html',{'salas_c':salas_c})
    else:
        
        if room_name=="añadir":
            
            if request.method == 'POST':
                salas_c = request.user.salas_c.all()
                nombre= request.POST.get('nombre','')
                salas = Salas.objects.filter(nombre__contains=nombre)[:8]
                
                return render(request,'chatapp/home.html',{'salas_c':salas_c,'salas':salas})   
            else:
                
                salas_c = request.user.salas_c.all()
                salas = Salas.objects.all()[:8]
                
                return render(request,'chatapp/home.html',{'salas_c':salas_c,'salas':salas})
        else:
        
            salas_c = request.user.salas_c.all()
            sala_obj=Salas.objects.get(id=room_name)
            mensajes= Mensajes.objects.filter(sala=sala_obj)
            sala_user=sala_obj.user
            
            return render(request,'chatapp/home.html',{'salas_c':salas_c,"room_name": room_name,'old_msg':mensajes,'salaUser':sala_user})
        
        
@login_required(login_url='/accounts/login')
def crear_sala(request):
    if request.method == 'POST':
        form = formularioCrearSala(request.POST,request.FILES)
        if form.is_valid():
            #form.save()
            if Salas.objects.filter(nombre=request.POST['nombre']):
                return render(request,'chatapp/c-sala.html',{'form':form,'msg':'Ya existe un nombre con esa sala'})
            else:
                nsala=Salas(nombre=request.POST['nombre'],imagen=request.FILES.get('imagen',''),user=request.user)
                nsala.save()
                sala_s=Salas_c(user=request.user,sala=nsala)
                sala_s.save()
                return redirect(to="/chat/")
    else:
        form = formularioCrearSala()
        return render(request,'chatapp/c-sala.html',{'form':form})
    
    
@login_required(login_url='/accounts/login')    
def borrar_sala(request,sala_id):
    
    sala = Salas.objects.get(id=sala_id)
    if request.method=='POST':
        if request.user == sala.user:
            sala.delete() 
            return redirect(to='/chat')
        else:
            return HttpResponse('No eres el propietario de la sala')
    else:
        return render(request,'chatapp/confirm.html',{'nombre_sala':sala.nombre})
    
              
@login_required(login_url='/accounts/login')
def guardar_sala(request,sala_id):
    
    sala = Salas.objects.get(id=sala_id)
    if Salas_c.objects.filter(sala=sala,user=request.user):
        return HttpResponse("Esa sala ya la tienes añadida")
    else:
        sala_g= Salas_c(user=request.user,sala=sala)
        sala_g.save()
        return redirect(to='/chat')
    
@login_required(login_url='/accounts/login')  
def borrar_sala_lista(request,sala_id):
    
    sala = Salas.objects.get(id=sala_id)
    if Salas_c.objects.filter(sala=sala,user=request.user):
    
        sala_b= Salas_c.objects.get(sala=sala,user=request.user)
        sala_b.delete()    
        return redirect(to='/chat')
    else:
        return HttpResponse("Esa sala no la tienes añadida")

"""
@login_required(login_url='/accounts/login/?next=/chat/')
def room(request, room_name):
    sala_obj=Salas.objects.get(id=room_name)
    mensajes= Mensajes.objects.filter(sala=sala_obj)
    return render(request, "chatapp/room.html", {"room_name": room_name,'old_msg':mensajes})
"""