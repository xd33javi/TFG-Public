from django.shortcuts import render,HttpResponse

# Create your views here.

from .models import Salas

def home(request):
    
    salas_v = Salas.objects.all()
    
    return render(request,'chatapp/home.html',{'salas_p':salas_v})