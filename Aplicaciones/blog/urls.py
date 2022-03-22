from django.urls import path

from .views import *
app_name = 'blog'
urlpatterns = [
    path('',home,name='index'),
    path('general',generales,name='generales'),
    path('tecnologia',tecnologia,name='Tecnologia'),
    path('programacion',programacion,name='Programacion'),
    path('videojuego',videojuegos,name='Videojuegos'),
    path('<slug:slug>/',detalles,name='detalles_post'),
]
