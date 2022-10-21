
#Django
from django.urls import path, include


#from rest_framework import routers

#rest_framework
from rest_framework import routers

#views

from canecas import views
app_name = 'canecas'

router = routers.DefaultRouter()
router.register(r'canecas_api', views.CanecaApiView,basename='canecas_api')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
    
    path('mi_caneca/<int:id>/', views.mi_caneca,name='mi_caneca' ),
    path('entregas/',views.entregas, name='entregas'),
    path('consultas/',views.consultar_canecas, name='consultas'),
    path('eliminar/<int:id>/',views.eliminar_canecas, name='eliminar'),
    path('buscar_canecas/<int:id_usuario>/', views.buscar_canecas,name='buscar_canecas'),
]