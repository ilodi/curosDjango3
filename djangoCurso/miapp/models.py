from django.db import models

# Create your models here.

# indicar que es un modelo


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(default='null')
    public = models.BooleanField()
    # solo se guarda la primera ves
    created_at = models.DateTimeField(auto_now_add=True)
    # se actualizara siempre
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # Guardad fecha de manera manueal
    crated_at = models.DateField()


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
