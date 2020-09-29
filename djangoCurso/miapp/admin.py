from django.contrib import admin
#mostrar los modelos en el admin Django
#1.- importat 
from .models import *

# Register your models here.
# Manipual modelos dentro del admin se pasa como segundo campo al methodo register
class ArticleAdmin(admin.ModelAdmin):
#solo lectura
    readonly_fields = ('created_at','updated_at')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)