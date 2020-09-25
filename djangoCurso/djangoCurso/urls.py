from django.contrib import admin
from django.urls import path

#Importat mis apps con mis vistas
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    path('inicio/', views.index , name="inicio"),
    path('pagina/', views.pagina , name="pagina"),
    path('pagina/<int:redirigir>', views.pagina , name="pagina"),
    path('hola-mundo/', views.hola_mundo , name="hola_mundo"),
    path('contacto/', views.contacto , name="contacto"),
    path('contacto/<str:nombre>', views.contacto , name="contacto"),
    path('contacto/<str:nombre>/<str:apellidos>', views.contacto , name="contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo, name="crear_articulo"),
    path('articulo/<str:title>/', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>/', views.editar_articulo, name="editar_articulo"),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar")
]
