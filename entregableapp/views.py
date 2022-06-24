
from re import template
from django.template import loader
from django.http import HttpResponse

from datetime import datetime
from entregableapp.models import Familia

# Create your views here.
def inicio(request):
    return HttpResponse("Bienvenido al mundo de la familia misteriosa")

def ver_fecha(request):
    fecha = datetime.now() 
    return HttpResponse(f"Fecha actual: {fecha}")

def plantilla(request):
    
    template = loader.get_template("primera_plantilla.html")
    render = template.render({})
    
    return HttpResponse(render)
    
   

def familia(request, integrante_nombre, integrante_edad):
    
    # dt = datetime.now()
    # integrante = Familia(nombre = integrante_nombre , edad = integrante_edad, fecha_creacion = dt)
    
    integrante = Familia(nombre = integrante_nombre , edad = integrante_edad)
    integrante.save()
    
    lista_familia = Familia.objects.all()
    
    template = loader.get_template("lista_familia.html")
    
    render = template.render({"lista" : lista_familia })
    
    return HttpResponse(render)