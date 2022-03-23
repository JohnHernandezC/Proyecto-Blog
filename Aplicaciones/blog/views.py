from django.http import QueryDict
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.core.paginator import Paginator

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
    
    pagina=Paginator(post,2)#esto pagina los post en este caso son 2 por pagina
    page=request.GET.get('page')#obtenemos la pagina actual
    post=pagina.get_page(page)#es para enviar al request solo los post pertenecientes a la pagina que se esta ejecutanddo
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
    queryset=request.GET.get('buscar')
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre__iexact='Tecnologia'))
    if queryset:
        post=Post.objects.filter(#filtrar por lo que se ingresa en la busqueda
            Q(titulo__icontains=queryset)|
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Tecnologia')
            
            ).distinct()
    return render(request,'blogt\gtecnologia.html',{'post':post})

def programacion (request):
    queryset=request.GET.get('buscar')
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre__iexact='Programacion'))
    if queryset:
        post=Post.objects.filter(#filtrar por lo que se ingresa en la busqueda
            Q(titulo__icontains=queryset)|
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='Programacion')
            
            ).distinct()
    return render(request,'blogt\programacion.html',{'post':post})

def videojuegos (request):
    queryset=request.GET.get('buscar')
    post=Post.objects.filter(estado=True, 
                             categoria=Categoria.objects.get(nombre__iexact='VideoJuegos'))
    if queryset:
        post=Post.objects.filter(#filtrar por lo que se ingresa en la busqueda
            Q(titulo__icontains=queryset)|
            Q(descripcion__icontains=queryset),
            estado=True,
            categoria=Categoria.objects.get(nombre__iexact='VideoJuegos')
            
            ).distinct()
    return render(request,'blogt\gvideojuegos.html',{'post':post})


