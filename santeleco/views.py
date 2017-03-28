from django.shortcuts import render
from django.http import HttpResponse
from .models import Grado, Actividad, Participante
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def barra(request):
	return HttpResponse("Hola, esto es San Teleco")

@csrf_exempt		#Cambia el comportamiento de esa función
def grado(request, identificador):

	if request.method == "POST":
		g = Grado(nombre=request.POST['nombre'])
		g.save()
		identificador = g.id

	try:
		g = Grado.objects.get(id=int(identificador))
		respuesta = "Soy el grado " + g.nombre
		return HttpResponse(respuesta)

	except Grado.DoesNotExist:
		respuesta = "No existo. Creame"
		respuesta += '<form action="" method="POST">'
		respuesta += 'Nombre: <input type="text" name="nombre">'
		respuesta += '<input type="submit" value="Enviar">'
		return HttpResponse(respuesta)
	
