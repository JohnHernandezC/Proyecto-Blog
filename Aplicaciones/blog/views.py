from django.shortcuts import render

from .models import *

def home (request):
    post=Post.objects.filter(estado=True)
    return render(request,'blogt\index.html',{'post':post})

def generales (request):
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre='General'))
                              #filtrado por estado y categoria
    return render(request,'blogt\generales.html',{'post':post})

def tecnologia (request):
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre='Tecnologia'))
    return render(request,'blogt\gtecnologia.html',{'post':post})

def programacion (request):
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre='Programacion'))
    return render(request,'blogt\programacion.html',{'post':post})

def videojuegos (request):
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre='VideoJuegos'))
    return render(request,'blogt\gvideojuegos.html',{'post':post})


