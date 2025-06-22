from django.shortcuts import render
from django.http import HttpResponse

def saludar (request):
    return HttpResponse("hola desde django") #clase httpResponse

def saludar_con_parametros(request, nombre: str , apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.upper()
    return HttpResponse (f"{apellido}, {nombre}")

def index(request):
    return render(request, "myapp/index.html")



# Create your views here.
#def index(request):
#    context = {"mensaje": "bienvenidos a mi aplicacion django"}
#    return render(request, "myapp/index.html", context)

#un context (en este caso "mensaje")es un diccionario en que la clave es lo que se le pasa al html
# y el valor en este caso ("bienvenidos a mi ....") lo uqe quier oque se pase al html como un contenido 
# return render(request(primercodigo), "myapp/index.html"(ubicacion), context(diccionario))


#el "mensaje" que esta en context es el <p>mensaje</p> que esta en index.html


# se necesita index, para cuando haga una solicitud al sitio web, se recibe como repuesta lo que tengamos en la funsion index(html) 