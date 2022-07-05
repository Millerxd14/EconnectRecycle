
from django.contrib import admin


from django.conf.urls.static import static
from django.conf import settings

from canecas import views as caneca_views

from rest_framework import routers


#router = routers.DefaultRouter()
#router.register(r'canecas_api', caneca_views.CanecaApiView)




from django.urls import path, include
from econciencia import views as econciencia_views


urlpatterns = [


    path('admin/', admin.site.urls),


    path('',include(('posts.urls', 'posts'), namespace='posts' )),
    path('users/',include(('users.urls', 'users'), namespace='users' )),
    path('caneca/',include(('canecas.urls', 'canecas'), namespace='canecas' )),


    path('fecha/', econciencia_views.dame_la_fecha_puto),
    path('datos_en_url/<int:edad>/<int:anio>', econciencia_views.recibirParametrosDeUrl, name='datos_url'),
    path('',econciencia_views.home,name="home"),


] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
