''' Econciencia middleware para usuarios'''

from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader, RequestContext


class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        # One-time configuration and initialization.

    def __call__(self, request):
        '''mensaje_error = {
                        'error': { 
                            'tipo' : 'error',
                            'titulo': 'Error',
                            'texto': 'Hola mundo',
                            'tiempo': '3000'
                        }
                    }
        '''
        if( not request.user.is_anonymous):
            profile = request.user.profile
            if not profile.person_type:
                if request.path not in [ reverse('actualizar_perfil'), reverse('logout')]:
                    return render(request, 'users/actualizar_perfil.html', {
                        'error': {
                            'tipo' :'notice',
                            'titulo':'Advertencia',
                            'texto':'Para poder continuar con la experiencia lo invitamos a completar su perfil',
                            'tiempo':'60000',
                        }
                    })
        response = self.get_response(request)
        return response