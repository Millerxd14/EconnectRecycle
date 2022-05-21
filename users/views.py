'''users views'''
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



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
    return render(request,'users/singup.html')


def recuperar_contrasena(request):
    pass


