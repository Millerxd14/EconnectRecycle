from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages




def dashboard(request ): # primera vista 
    context = {'mensaje': 'hola mundo'}
    return render(request, 'dashboard.html',context)


def dame_la_fecha_puto(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse("<h3> La hora actual es %s</h3>" %fecha_actual)



def recibirParametrosDeUrl(request, edad,anio):
    
    periodo = anio - 2021
    edad_futura = edad+periodo
    return HttpResponse("<h3> En el año  %s tendras %s años, un saludo muy cordial</h3>" %(anio,edad_futura))


def login(request):
    return render(request, 'login.html',
    {
        "saludo": 'Hola mundo usando Diccionario',
        'harold': "HArold es puto"
    })



def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado exitosamente')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html',context)


