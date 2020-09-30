from django.contrib import admin
from django.urls import path
#para cargar images
from django.conf import settings

# Importat mis apps con mis vistas
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('pagina/', views.pagina, name="pagina"),
    path('pagina/<int:redirigir>', views.pagina, name="pagina"),
    path('hola-mundo/', views.hola_mundo, name="hola_mundo"),
    path('contacto/', views.contacto, name="contacto"),
    path('contacto/<str:nombre>', views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellidos>',
         views.contacto, name="contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>',
         views.crear_articulo, name="crear_articulo"),
    path('articulo/<str:title>/', views.articulo, name="articulo"),
    path('editar-articulo/<int:id>/',
         views.editar_articulo, name="editar_articulo"),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar-articulo/<int:id>', views.borrar_articulo, name="borrar"),
    # formulario
    path('save-article/', views.save_article, name="save"),
    path('create-article/', views.create_article, name="create"),
    path('create-full-article/', views.create_full_article, name="create_full"),
]

#configuracion para cargar imagenes
#cargar ficheros como si fueran statios
#1.- Import settings
#2.- Que el comprobar que el proyecto este en modo debuug solo es para test ya en linea si funciona
if settings.DEBUG:
    from django.conf.urls.static import static
#3.- tomar toda la lista de url y concatena una nueva url
#primero se para la url y luego el root
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)