'''users views'''
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

#models

from django.contrib.auth.models  import User
from users.models import Profile

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
        username = request.POST.get('usuername')
        password = request.POST['password']        
        confirm_password = request.POST['confirm_password']        
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']        
        email = request.POST['email']        
        user_type = request.POST['user_type']  
        if(password != confirm_password):
            return render(request,'users/singup.html',{
                'error': 'Las contraseñas no coinciden'
            })
        user = User.objects.create_user(username =username, password = password)
        user.firts_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        profile = Profile(user = user, )


    return render(request,'users/singup.html')


def recuperar_contrasena(request):
    pass


