
from django.contrib import admin


from django.conf.urls.static import static
from django.conf import settings


from django.urls import path
from econciencia import views as econciencia_views
from users import views as users_views
from posts import views as posts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', users_views.login_view, name="login"),
    path('logout/', users_views.logout_view, name="logout"),
    path('singup/',users_views.singup, name='singup'),
    path('fecha/', econciencia_views.dame_la_fecha_puto),
    path('datos_en_url/<int:edad>/<int:anio>', econciencia_views.recibirParametrosDeUrl, name='datos_url'),
    path('',econciencia_views.home,name="home"),
    path('posts/latest_posts/',posts_views.latest_posts,name="latest_posts"),
    path('recuperar_contrasena/', users_views.recuperar_contrasena, name="recuperar_contrasena"),
    path('perfil/actualizar_perfil/', users_views.update_profile, name='actualizar_perfil'),
    path('mi_caneca/', econciencia_views.mi_caneca,name='mi_caneca' ),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
