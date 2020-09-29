from django.db import models

# Create your models here.

# indicar que es un modelo


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null',verbose_name="Imagen")
    public = models.BooleanField(verbose_name="¿Publicado?")
    # solo se guarda la primera ves
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    # se actualizara siempre
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    #clase meta en los modelos ayuda a proporcionar informacion al admin
    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering = ['created_at']
    #methodo magico para que el objeto sea humanisado en el admin
    def __str__(self):
        if self.public:
            publico = "(publicado)"
        else:
            publico = "(privado)"
        return f"{self.title}  {publico}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # Guardad fecha de manera manueal
    crated_at = models.DateField()
    class Meta:
        verbose_name="Categoría"
        verbose_name_plural="Categorías"


"""
1.- Tener los modelos
2.- Crear la migracion para crear las tablas
'python manage.py makemigrations'
3.- Crear SQL
'python manage.py sqlmigrate miapp 001'
4.- Ejecutar | guardar en la base de datos ya
'python manage.py migrate'
----------------------------------------------------
Hacer modificaciones en campos/modelos ya existentes
----------------------------------------------------
1.- Tener cambios
2.- 'python manage.py makemigrations'
3.- 'python manage.py sqlmigrate NOMBRE DE APP NUMERO DE MIGRACION'
4.- 'python manage.py migrate'
"""
