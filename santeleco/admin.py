from django.contrib import admin

# Register your models here.

from .models import Participante
from .models import Actividad
from .models import Grado

admin.site.register(Participante)
admin.site.register(Actividad)
admin.site.register(Grado)
