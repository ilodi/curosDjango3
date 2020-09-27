from django.shortcuts import render, HttpResponse, redirect
# importar modelo para hacer uso de el
from miapp.models import Article
#agregar OR para consultas
from django.db.models import Q

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
    # lista
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

    return render(request, 'pagina.html', {
        'text': '',
        'lista': ['uno', 'dos', 'tres']
    })


def contacto(request, nombre="", apellidos=""):
    html = ""
    if nombre and apellidos:
        html = f"<h3>Nombre completo {nombre} {apellidos}</h3>"
    return HttpResponse(layout + f"<h1>Contacto </h1>"+html)


def crear_articulo(request, title, content, public):
    """
    1.- importat el modelo
    2.- paso acontinuacion instanciar la clase
    """
    articulo = Article(
        title=title,
        content=content,
        public=public
    )
    """
    3.- Guardar en la base de datos
    """
    articulo.save()

    return HttpResponse(f"Articulo creado:{articulo.title} - {articulo.content }")


def articulo(request, title):
    """
    Hacer una consulta a la base de datos
    1.- de la instancia del modelo se usa el .objects 
    Objects ::Accede al modelo -> Accede a su objetos para hacer la consulta
    como objects trae todo lo de el modelo se usa el .get() para ser mas especifico
    """
    """
    para que el get funcione le puedes mandar un id
    el cual se consulta con un pk = primary key,
    de igual manera con cualquier entidad de la base de datos
    el id es la que todas tienen en comun pero igual esta 
    todas las que has creado...
    tambien puedes ser más especifico agregando mas parametros como
    get(x,y)
    """
    # para evitar errores un try y un except
    try:
        articulo = Article.objects.get(title=title)
        response = f"Articulo id:{articulo.id}-{articulo.title}"
    except:
        response = "No se encuentra el articulo"

    return HttpResponse(response)


def editar_articulo(request, id):
    """
    ediart articulo
    1.- instanciar del modelo para la consulta
    """
    articulo = Article.objects.get(pk=id)
    """
    2.-Dar valor a sus propiedades
    """
    articulo.title = "Feri"
    articulo.content = "Nueva"
    articulo.public = True
    """
    3.-Guardar valores
    """
    articulo.save()

    return HttpResponse(f"Articulo editado id:{articulo.id}-{articulo.title}")


def articulos(request):
    # caso 1
    """
    Traer todos los articulos
    1.- hacer consulta
    2.- el metodo .all trae todo
    all trae todo y order_by ordena por lo que se necesite
    para ordenar de manera inversa solo agrega - ejemplo
    .order_by('-name')
    .order_by('-id)
    limite de  consula
    .order_by('id')[:x]
    limite de sonsulta entre z y y
    .order_by('id')[x:y]
    sacar solo un elemento
    .order_by('id')[0:1]

    """
    articulos = Article.objects.all()

# caso 2
    """
    hacer más consultas especificas
    -- Metodo filter()
    """
    """
    todos los campos tienen un lookup el cual se ejecuta x__lookup
    ejemplo que el titulo tenga la palabra articulos
    title__container="articulo"
    o que sean exactamante un valor
    title__exact="algo"
    si necesitas que no importen mayusculas o minusculas usas
    title_iexact="algo"
    """
    """
    lookup_gt == mas grande que
    sacar los que tengan un id mayor a 12
    id__gt=12
    lookup_gte == mayor o igual que
    sacar el mayor o igual a 11
    id__gte=11
    lookup_lte == menores o igual que
    sacar el menor o igual a 11
    id_lte=11
    por ultimo puedes hacer mas de una filtracion de la siguiente manera
    """
    articulos = Article.objects.filter(id__lte=11, title__contains="Articulo")

   # caso 3
    """
        obtener articulos que solo esten publicados
        1.-hacer consulta
        2.- usar el .filter(public=True)
        ///es como un segundo filtro para extraer
        .---Tambien puedes usar filter().exclude()
    """
    articulos = Article.objects.filter(title="Articulo").exclude(public=False)

    #Sql crudo
    articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Artiuclo' AND public=0 ")
    
    #caso 4 
    """
    agregar OR a las rutas
    1.- importar
    from django.db.models import Q
    2.- usar .filter(Q(X) | Q(Y) )
    """
    articulos = Article.objects.filter(Q(title__contains="2") | Q(title__contains="3"))
    return render(request, 'articulos.html', {
        'articulos': articulos
    })


def borrar_articulo(request, id):
    """
    borrar articulo
    1.- hacer consulta
    """
    articulo = Article.objects.get(pk=id)
    """
    2.- ya que lo tengas con su id se borra
    """
    articulo.delete()

    return redirect('articulos')
