from django import forms
from django.contrib.auth.models import User
from canecas.models import Caneca

class CreateCaneca(forms.Form):
    user = forms.CharField(min_length=4)
    name = forms.CharField(min_length=5)
    description = forms.CharField(min_length=4, max_length=30)
    mac  = forms.CharField(max_length=15)
    direction = forms.CharField(max_length=50)
    def clean_usuario(self):
        user = self.cleaned_data['usuario']
        username_use = User.objects.get(username=user)
        return username_use
    def save(self):
        '''create caneca mamadisima'''
        data = self.cleaned_data
        print(data['direction'])
        user = data['user']
        username_use = User.objects.get(username=user)

        name = data['name']
        description = data['description']
        mac = data['mac']
        ubicacion = data['direction']
        
        caneca = Caneca()
        caneca.user= username_use
        caneca.name = name
        caneca.description = description
        caneca.mac = mac
        caneca.ubicacion = ubicacion

        caneca.save()
        
    

