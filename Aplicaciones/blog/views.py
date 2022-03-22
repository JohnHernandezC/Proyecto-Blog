from django.http import QueryDict
from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import *

def home (request):
    print(request.GET)#con esto podemos capturar como esta llegano un valor enviado pos Get
    queryset=request.GET.get('buscar')
    post=Post.objects.filter(estado=True)
    if queryset:
        post=Post.objects.filter(#filtrar por lo que se ingresa en la busqueda
            Q(titulo__icontains=queryset)|
            Q(descripcion__icontains=queryset)
            ).distinct()
    
    
    return render(request,'blogt\index.html',{'post':post})

def detalles (request,slug):
    post=get_object_or_404(Post,slug=slug)
    #post=Post.objects.get(slug=slug)#ta same shit pero sin la comprobacion
    return render(request,'blogt\post.html',{'detalle_post':post})#obtener la informacion de un post

def generales (request):
    queryset=request.GET.get('buscar')
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre__iexact='general'))#
                              #(__iexact) Muy importante nos filtra sin importar mayusculas o minusculas
                              #filtrado por estado y categoria
    if queryset:
        post=Post.objects.filter(#filtrar por lo que se ingresa en la busqueda
            Q(titulo__icontains=queryset)|
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='general')
            
            ).distinct()
        
    return render(request,'blogt\generales.html',{'post':post})

def tecnologia (request):
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre__iexact='Tecnologia'))
    return render(request,'blogt\gtecnologia.html',{'post':post})

def programacion (request):
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre__iexact='Programacion'))
    return render(request,'blogt\programacion.html',{'post':post})

def videojuegos (request):
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre__iexact='VideoJuegos'))
    return render(request,'blogt\gvideojuegos.html',{'post':post})


