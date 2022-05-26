''' Users models '''

from django.db import models


from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    '''
        Profile model
        Proxy model that extends ther base data with other information
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    direction = models.CharField(max_length= 100, blank=False)
    phone_number = models.CharField(max_length=15, blank=True)
    person_type = models.IntegerField(blank=True, null=True)

    profile_picture = models.ImageField(upload_to='users/pictures',blank=True,null=True)
    company_name = models.CharField(max_length=200,blank=True)
    is_collector = models.BooleanField(default=True)
    is_productor = models.BooleanField(default=False)

    dni = models.CharField(max_length=20,default='unamed')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)


    def __str__(self):
        '''return username '''
        return self.user.username

'''
    Como hacer insertar registros y hacer busquedas ? 

    from app.models import class #se debe importar la clase a instanciar para cualquier caso
    #luego se instancia un objeto de ese tipo

    nombre_clase = Clase( atributo_1 = 'nombre', atributo_2 = '')  
    nombre_clase.save()

    #otra forma sería así, directamente 
    nombre_clase = Clase.objects.create(atributo_1 = 'nombre', atributo_2 = '')

    #para buscar uno solo escribir    

    objeto_buscado = Class.objects.get( usuario = 'Miller')# equivalencias exactas
    # para busquedas que coincidan con ... o demás es 
    varios_resultados = Class.objects.filter(usuario__endswith = 'Hurtado' ) # esta consulta me vota varios usuarios
    varios_resultados = Class.objects.all() # devuelve todo de la bd
    # el get solo me trae un resultado, con el filte puedo aplicar filtros xD y me devuelve varios registros de bd
    # Existen más filtros, para eso consulte la documentacion de django  3.2.4
    # para actualizar varios datos con la opción .update(valores)
    varios_resultados = Class.objects.filter(usuario__endswith = 'Hurtado' ).update(nombre= 'todos somos miller ahora')# esto cambia el nombre a  todos los usuarios que terminan en hurtado
    #update devuelve un entero del numero de registros que actualizó

'''