'''users views'''
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

#forms 

from users.forms import ProfileForm, SingUpForm
from users.models import Profile

# except careverga
from django.db.utils import IntegrityError
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
            return redirect('users:login')
    else: 
        form = SingUpForm()

    return render(request,'users/singup.html',{
        'form':form
    })


def recuperar_contrasena(request):
    pass

def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
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

    return render(request, 'users/actualizar_perfil.html',{
        'profile': profile,
        'user': request.user,
        'form': form
    })



@login_required
def recolectores(request):
    profile = request.user.profile
    user = request.user
    #buscar recolectores por usuario en 
    recolectores = Profile.objects.filter(is_collector = 1)
    context ={
        'profile': profile,
        'user': request.user,
        'recolectores':recolectores,
    }
    return render(request, 'users/recolectores.html',context)



@login_required
def productores(request):
    profile = request.user.profile
    
    productores = Profile.objects.filter(is_productor = 1)
    context = {
        'profile': profile,
        'user': request.user,
        'productores': productores,
    }
    return render(request, 'users/productores.html',context)
