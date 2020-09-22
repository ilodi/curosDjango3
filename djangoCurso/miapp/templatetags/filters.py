#crear un nuevo filtro
from django import template

#se extancia 
register = template.Library()

#decorador
# es una funcionalidad previa a una funcion 
@register.filter(name='saludo')
def saludo(value):
    if len(value) >= 8:
        largo = '<p>Tu nombre es muy largo</p>'
    return f"<h1 style='background:green; color:white'>Bienvenido: {value} </h1> "+largo