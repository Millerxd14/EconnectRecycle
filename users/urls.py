''' Users views '''


#Django 
from django.urls import path


#Models

from users import views

urlpatterns = [
    path(
        route ='login/',
        view = views.login_view, 
        name="login"
    ),
    path(
        route ='logout/',
        view = views.logout_view, 
        name="logout"
    ),
    path(
        route ='singup/',
        view =views.singup, 
        name='singup'
    ),
    path(
        route ='recuperar_contrasena/',
        view = views.recuperar_contrasena, 
        name="recuperar_contrasena"
    ),
    path(
        route ='perfil/actualizar_perfil/',
        view = views.update_profile, 
        name='actualizar_perfil'
    ),
    path(
        route ='recolectores/',
        view = views.recolectores, 
        name='recolectores'
    ),
    path(
        route ='productores/',
        view = views.productores, 
        name='productores'
    ),
    path(
        route='formulario_recolectores',
        view=views.advance_update_profile,
        name="formulario_recolectores"
    ),
    path(
        route='buscar_recolector',
        view=views.buscar_recolector,
        name = 'buscar_recolector'
    ),
    path(
        route='aceptar_recolector/<int:id_info>',
        view=views.aceptar_recolector,
        name = 'aceptar_recolector'
    ),
    path(
        route='aceptar_productor/<int:id>',
        view=views.aceptar_productor,
        name = 'aceptar_productor'
    ),
    path(
        route='rechazar_visualizacion/<str:tipo>/<int:id>',
        view=views.rechazar_visualizacion,
        name = 'rechazar_visualizacion'
    ),
    path(
        route='datos_usuario/<int:id>',
        view=views.datos_usuario,
        name = 'datos_usuario'
    ),
]