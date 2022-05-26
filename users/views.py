'''users views'''
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

#models

from django.contrib.auth.models  import User
from users.models import Profile


# except careverga
from django.db.utils import IntegrityError
# Create your views here.
def login_view(request):
    '''Login view'''
    if request.method == 'POST':
       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password= password)
        if user:
            login(request,user)
            return redirect('latest_posts')
        else:
            return render(request, 'users/login.html',
            {
                "error": 'Error, usuario y contraseña invalidos',
            })

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    '''logout user'''
    logout(request)
    return redirect('login')

def singup(request):
    '''sing up view'''
    
    if(request.method == "POST"):
        password = request.POST['password'] 
        confirm_password = request.POST['confirm_password']        
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']        
        email = request.POST['email']        
        user_type = request.POST['user_type'] 
        print
        # Tocó en español porque en ingles la muy zorra no sirve
        usuario = request.POST['usuario']
        #import pdb;pdb.set_trace()
               
         
        if(password != confirm_password):
            return render(request,'users/singup.html',{
                'error': 'Las contraseñas no coinciden'
            })
        if(user_type == '0'):
            return render(request,'users/singup.html',{
                'error': 'Debes escoger un tipo de usuario valido'
            })
        elif user_type == '1':
            is_productor_field = 1
            is_collector_field = 0
        elif user_type == '2':
            is_productor_field = 0
            is_collector_field = 1
        try:
            user = User.objects.create_user(username = usuario,email = email,password = password)
        except IntegrityError:
            return render(request,'users/singup.html',{
                'error': 'El usuario que escogiste ya está en uso'
            })
        user.first_name = first_name
        user.last_name = last_name
        
        user.save()
        profile = Profile(user = user, is_productor = is_productor_field, is_collector = is_collector_field )
        profile.save()
        return render(request,'users/login.html')


    return render(request,'users/singup.html')


def recuperar_contrasena(request):
    pass


