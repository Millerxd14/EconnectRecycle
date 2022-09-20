from email.policy import default
from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.password_validation import validate_password

from users.models import Profile

class SingUpForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField( widget=forms.PasswordInput)
    password_confirmation = forms.CharField( widget=forms.PasswordInput)

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)



    email = forms.CharField(min_length=6,max_length=50, widget=forms.EmailInput() )

    #Tipo de Usuario
    tipos_usuario = [
        ('0', '¿ Que tipo de usuario eres ?'),
        ('1', 'Recolector de residuos'),
        ('2', 'Productor de residuos'),
    ]
    tipo_usuario = forms.ChoiceField( 
        widget=forms.Select,
        choices=tipos_usuario
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        email_use = User.objects.filter(email = email).exists()
        if email_use:
            raise forms.ValidationError('Ese correo ya está en uso')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        username_use = User.objects.filter(username = username).exists()
        if username_use:
            raise forms.ValidationError('Ese usuario ya está en uso')
        return username

    def clean(self):
        data = super().clean()
    
        password = data['password']
        password_confirmation = data['password_confirmation']

        if(password != password_confirmation):
            raise forms.ValidationError('Las contraseñas no coinciden')
        else:
            validate_password(password=password)

        if data['tipo_usuario'] == '0':
            raise forms.ValidationError(' Selecciona un tipo de usuario ')

        if(data['tipo_usuario'] == '1'):
            data['is_collector'] = 1
            data['is_productor'] = 0
        else:
            data['is_collector'] = 0
            data['is_productor'] = 1

        return data

    def save(self):
        '''create user'''
        data = self.cleaned_data
        data.pop('password_confirmation')
        is_collector = data['is_collector']
        is_productor = data['is_productor']
        data.pop('is_collector')
        data.pop('is_productor')
        data.pop('tipo_usuario')
        user = User.objects.create_user(**data)
        profile = Profile(user = user, is_collector = is_collector, is_productor = is_productor)
        profile.save()








class ProfileForm(forms.Form):
    
    tipos_documento = [
        ('0', 'Tipo de persona'),
        ('1', 'Natural'),
        ('2', 'Juridica'),
    ]
    person_type = forms.ChoiceField(
        widget=forms.Select,
        choices=tipos_documento)

    profile_picture = forms.ImageField(required=False)
    dni = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20,required=True)
    direction = forms.CharField(max_length=100, required=True)

    
    company_name = forms.CharField(max_length=30)


class AdvanceProfileForm(forms.Form):
    description = forms.TextInput()

    plastic = forms.IntegerField()
    plastic_price = forms.IntegerField()


    cardboard = forms.IntegerField()
    cardboard_price = forms.IntegerField()


    paper = forms.IntegerField()
    paper_price = forms.IntegerField()


    glass = forms.IntegerField()
    glass_price = forms.IntegerField()

    trash = forms.IntegerField()
    trash_price = forms.IntegerField()

    metal = forms.IntegerField()
    metal_price = forms.IntegerField()

