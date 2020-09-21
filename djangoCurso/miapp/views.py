from django.shortcuts import render, HttpResponse, redirect

# MVC = Modelo Vista Controlador
# Dentro del controlador hay Acciones(metodos)
# MVT = Modelo Template Vista
# En Django dentro de las vistas hay Acciones (metodos)
# modo ramido invert filter: invert(1) hue-rotate(180deg);

layout = """
<h1>Sitio web</h1>
<hr/>
<ul>
    <li>
        <a href="/">Inicio</a>
    </li>
     <li>
        <a href="/hola-mundo">Hola mundo</a>
    </li>
     <li>
        <a href="/pagina">Pagina prueba</a>
    </li>
     <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""


def index(request):
    """
    template = ""<h1>Inicio</h1>
    <p>Años hasts 2050:</p>
    <ul>""
    year = 2021
    while year <= 2050:
        if year % 2 == 0:
            template += f"<li>{str(year)}</li>"
        year += 1

    template += "</ul>"
    """
    year = 2021
    hasta = range(year, 2051)
    nombre = "lodo"
    #lista
    lenguajes = ['js', 'python', 'c']
    # para pasar informacion es el 3 parametro y esta es en formato diccionario
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })


def hola_mundo(request):
    return render(request, 'hola_mundo.html')


def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect('contacto', nombre="Eduardo", apellidos="diaz")

    return render(request, 'pagina.html')


def contacto(request, nombre="", apellidos=""):
    html = ""
    if nombre and apellidos:
        html = f"<h3>Nombre completo {nombre} {apellidos}</h3>"
    return HttpResponse(layout + f"<h1>Contacto </h1>"+html)
