from django.http import HttpResponse
import datetime

def dashboard(request): # primera vista 

    return HttpResponse("<h5>Hola mundo mundial xD</h5>")


def dame_la_fecha_puto(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse("<h3> La hora actual es %s</h3>" %fecha_actual)



def recibirParametrosDeUrl(request, edad,anio):
    
    periodo = anio - 2021
    edad_futura = edad+periodo
    return HttpResponse("<h3> En el año  %s tendras %s años, un saludo muy cordial</h3>" %(anio,edad_futura))

