from django.db import models

# Create your models here.

class Grado(models.Model):
	nombre = models.CharField(max_length=128)

class Actividad(models.Model):
	actividad = models.CharField(max_length=128)
	deportiva = models.BooleanField()
	dia = models.DateField()
	lugar = models.CharField(max_length=128)


class Participante(models.Model):
	nombre = models.CharField(max_length=128)
	grado = models.ForeignKey(Grado)								#Relación 1 a N con Grado -> 1 Grado pueden hacerlo N Participantes, pero 1 Participante sólo puede hacer 1 Grado
	curso = models.IntegerField()
	#actividad = ManyToManyField('self', symmetrical=False)			#Relación N a N con Actividad -> 1 Actividad pueden hacerla N Participantes y 1 Participante puede hacer N Actividades
	actividad = models.ForeignKey(Actividad)						#Relación 1 a N con Actividad -> 1 Actividad pueden hacerla N Participantes, pero 1 Participante sólo puede hacer 1 Actividad


	



#Para simplificar, primero sin relaciones N a N. De momento cada participante sólo puede hacer 1 Actividad.
#1. Se empieza siempre por el diseño del MODELO, es decir , haciendo models.py
#2. Se añade la aplicación a settings.py dentro de INSTALLED_APPS
#3. Para compilar se ejecuta: python3 manage.py makemigrations
#4. Cuando se consiguen quitar todos los errores se ejecuta: python3 manage.py migrate
#5. Registrar el modelo en admin.py
#6. Configurar urls.py
#7. Configurar views.py
