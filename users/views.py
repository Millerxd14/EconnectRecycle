'''users views'''

'''Otras cositas'''
import json
from datetime import date
from django.db import IntegrityError

# django
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from notifications_app.models import BroadcastNotification

#forms 
from users.forms import ProfileForm, SingUpForm, AdvanceProfileForm
from users.models import Info_Recolector, Profile, VProductorRecolector

# except careverga
from django.contrib.auth.models import User




def login_view(request):
    '''Login view'''
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password= password)
        if user:
            login(request,user)
            return redirect('posts:latest_posts')
        else:
            return render(request, 'users/login.html',
            {
                'error': { 
                    'tipo' : 'error',
                    'titulo': 'Error',
                    'texto': 'Usuario y contraseña invalidos',
                    'tiempo': '2000'
                    }
            })

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    '''logout user'''
    logout(request)
    return redirect('users:login')

def singup(request):
    '''sing up view'''
    
    if(request.method == "POST"):
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else: 
        form = SingUpForm()

    return render(request,'users/singup.html',{
        'form':form
    })


def recuperar_contrasena(request):
    pass

def update_profile(request):
    #import pdb;pdb.set_trace()
    profile = request.user.profile   
    form_advance = ''
    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)
        
        if profile.update_counter == 1:
            updated_request = request.POST.copy()
            updated_request.update({'person_type': profile.person_type})
            updated_request.update({'dni': profile.dni})
            form = ProfileForm(updated_request, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            profile.company_name = data['company_name']
            profile.direction = data['direction']
            profile.phone_number = data['phone_number']
            profile.profile_picture = data['profile_picture']
            profile.dni = data['dni']
            profile.person_type = data['person_type']
            profile.save()
            return redirect( 'users:actualizar_perfil' )

    else:
        form = ProfileForm()
        if(profile.is_collector == 1):
            form_advance = AdvanceProfileForm()         
    
    if(profile.is_collector == 1):
            info_recolector = Info_Recolector.objects.get(profile = profile)
    else:
        info_recolector = ''



    bandera = 0
    if(profile.update_counter == 1):
        bandera = 1


    return render(request, 'users/actualizar_perfil.html',{
        'profile': profile,
        'info_recolector':info_recolector,
        'user': request.user,
        'form': form,
        'form_advance': form_advance,
        'bandera': bandera
    })


@login_required
def advance_update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form_advance = AdvanceProfileForm(request.POST)
        #import pdb;pdb.set_trace()
        if form_advance.is_valid():
            
            form_advance.save(profile)
            return redirect( 'users:actualizar_perfil' )
        
        return redirect('users:actualizar_perfil')

@login_required
def recolectores(request):
    profile = request.user.profile
    user = request.user
    #buscar recolectores por usuario en 
    recolectores = Info_Recolector.objects.all()
    context ={
        'profile': profile,
        'user': request.user,
        'recolectores':recolectores,
    }
    return render(request, 'users/recolectores.html',context)



@login_required
def productores(request):
    profile = request.user.profile
    usuarios_aceptados = VProductorRecolector.objects.filter(recolector= request.user)
    context = {
        'profile': profile,
        'user': request.user,
        'productores': usuarios_aceptados,
    }
    return render(request, 'users/productores.html',context)




@login_required
def buscar_recolector(request):
    if request.method == 'POST':
        return 0
    else:
        texto = request.GET['texto_usuario']
        residuo = request.GET['residuo']
        filtro_residuo = Q(profile__company_name__contains=texto)
        if(residuo == 'plastic'):
            filtro_residuo = Q(plastic = 1)
        elif(residuo == 'glass'):
            filtro_residuo = Q(glass = 1)
        elif(residuo == 'metal'):
            filtro_residuo = Q(metal = 1)
        elif(residuo == 'cardboard'):
            filtro_residuo = Q(cardboard = 1)
        elif(residuo == 'trash'):
            filtro_residuo = Q(trash = 1)
        elif(residuo == 'paper'):
            filtro_residuo = Q(paper = 1)
        recolectores = Info_Recolector.objects.filter( 
            (Q(profile__user__username__contains=texto) | 
            Q(profile__company_name__contains=texto)) & 
            filtro_residuo)
        data = {}
        i= 0
        for recolector in recolectores:
            data[i] = {
                'company_name'  : recolector.profile.company_name,
                'username': recolector.profile.user.username, 
                'description': recolector.description,
                'plastic'       : recolector.plastic,
                'glass'        : recolector.glass,
                'metal'        : recolector.metal,
                'cardboard'    : recolector.cardboard,
                'trash'        : recolector.trash,
                'paper'        : recolector.paper
                }
            i = i+1
        return JsonResponse(data)


@login_required
def aceptar_recolector(request, id_info):

    info = Info_Recolector.objects.get(id = id_info)
    recolector = info.profile.user
    productor = request.user
    mensaje = 'El usuario '+ productor.username +' quiere comunicarse contigo'
    try:
        nueva_visualizacion = VProductorRecolector(
            autoriza_recolector = 0,
            autoriza_productor = 1,
            productor = productor,
            recolector = recolector
        )
        

        notificacion = BroadcastNotification(
            mensaje = mensaje, 
            estado = 0, 
            broadcast_on= date.today(), 
            usuario_propietario = recolector, 
            usuario_enviador=productor,
            direccion = 'users:productores'
        )
        nueva_visualizacion.save()
        notificacion.save()
        return JsonResponse({
            'titulo' : 'Exito !',
            'mensaje': 'Notificacion enviada, pronto se comunicarán contigo',
            'tipo': 'success'
        })
    except IntegrityError:
        return JsonResponse({
            'titulo' : 'Ups !',
            'mensaje': 'Ocurrió un error inesperado, comprueba que no hayas  aceptado a este recolector antes',
            'tipo': 'error'
        })
    
@login_required
def aceptar_productor(request, id):
    productor  = User.objects.get(id = id)
    recolector = request.user
    mensaje = 'El recolector '+ recolector.username +' aceptó la comunicación contigo'

    visualizacion = VProductorRecolector.objects.get(
        productor = productor,
        recolector = recolector
    )
    datos_productor = Profile.objects.get(user = productor)
    print(visualizacion.productor.id, visualizacion.recolector.id, visualizacion.autoriza_recolector)
    if(visualizacion.autoriza_recolector == '0'):
        print('Entras ??')
        visualizacion.autoriza_recolector = 1
        visualizacion.save()

        notificacion = BroadcastNotification(
            mensaje = mensaje, 
            estado = 0, 
            broadcast_on= date.today(), 
            usuario_propietario = productor, 
            usuario_enviador=recolector,
            direccion = 'users:recolectores'
        )

        notificacion.save()
        
        return JsonResponse({
            'titulo' : 'Exito !',
            'mensaje': 'Notificacion enviada, pronto se comunicarán contigo',
            'tipo': 'success',
            'telefono_productor': datos_productor.phone_number,
            'correo_productor':productor.email,
        })
    else:
        return JsonResponse({
            'titulo' : 'Alerta !',
            'mensaje': 'Ya has aceptado a este productor previamente',
            'tipo': 'notice',
            'telefono_productor': datos_productor.phone_number,
            'correo_productor':productor.email,
        })
