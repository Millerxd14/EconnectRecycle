''' Users views '''


#Django 
from django.urls import path


#Models

from users import views

urlpatterns = [
    path(
        route ='users/login/',
        view = views.login_view, 
        name="login"
    ),
    path(
        route ='users/logout/',
        view = views.logout_view, 
        name="logout"
    ),
    path(
        route ='users/singup/',
        view =views.singup, 
        name='singup'
    ),
    path(
        route ='users/recuperar_contrasena/',
        view = views.recuperar_contrasena, 
        name="recuperar_contrasena"
    ),
    path(
        route ='users/perfil/actualizar_perfil/',
        view = views.update_profile, 
        name='actualizar_perfil'
    ),


]