
#django
from pprint import pprint
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


#Api libraries
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from canecas.serializers import CanecaSerializer



#models

from canecas.models import Caneca
from canecas.forms import CreateCaneca
from canecas.script_ia import model_ia

#Otras librerias
import numpy as np
from PIL import Image



class CanecaApiView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to edit Canecas or predict an image.
    """

    serializer_class = CanecaSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=True, methods=['post'])
    def solve_image(self, request, pk=None):
        caneca = Caneca.objects.get(pk=pk)
        
        n_peticiones = caneca.n_peticiones + 1
        caneca.n_peticiones = n_peticiones
        caneca.save()

        if(request.FILES):

            img = Image.open(request.FILES['file'])
            image_solve = model_ia.predict_external_image(img)
           

            return Response(
                {
                    'status': '200',
                    'message': 'Your image was predict',
                    'image_solve': image_solve
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                'status': '400',
                'message': 'Bad request, you must send a image'
                },
                status= status.HTTP_400_BAD_REQUEST
            )

    def list(self, request):
        user = request.user
        queryset = Caneca.objects.filter(user = user)
        serializer = CanecaSerializer(queryset, many=True)
        return Response(serializer.data)



    def retrieve(self, request, pk=None):
        user = request.user
        queryset = Caneca.objects.filter(user = user)#3,54,5,3
        caneca = get_object_or_404(queryset, pk=pk)
        serializer = CanecaSerializer(caneca)
        return Response(serializer.data)


    def create(self, request):
        return Response(
                {
                'status': '400',
                'message': 'You are not allowed to create or delete'
                },
                status= status.HTTP_400_BAD_REQUEST
            )

    

    def destroy(self, request, pk=None):
         return Response(
                {
                'status': '400',
                'message': 'You are not allowed to create or delete'
                },
                status= status.HTTP_400_BAD_REQUEST
            )



    def update(self, request, pk=None):
        user = request.user
        canecas_user = Caneca.objects.filter(user = user)
        caneca = Caneca()
        try:
            caneca = Caneca.objects.get(pk=pk)
            if( caneca in canecas_user ):
                serializer = CanecaSerializer(caneca, data = request.data, partial =True)
                if(serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {
                        'status': '400',
                        'message': 'Invalid Caneca id'
                    },
                    status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {
                    'status': '400',
                    'message': 'Invalid Caneca id'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    
    
@login_required
def mi_caneca(request,id):
    caneca = Caneca.objects.get(id=id)
    profile = request.user.profile
    
    if request.method == 'POST':
        form = CreateCaneca(request.POST)
        if form.is_valid():
            form.save()
            return redirect('canecas:consultar_caneca',id=1)
    else:
        form = CreateCaneca()


    #import pdb;pdb.set_trace()
    data = []
    
    
    
    
    data.insert(0,caneca.trash)
    data.insert(0,caneca.cardboard)
    data.insert(0,caneca.glass)
    data.insert(0,caneca.metal)
    data.insert(0,caneca.paper)
    data.insert(0,caneca.plastic)

    context = {
        'profile': profile,
        'form': form,
        'caneca': caneca,
        'data': data
    }

    return render(request, 'canecas/mi_caneca.html',context)


#@login_required
def entregas(request):
    #profile = request.user.profile
    #'profile': profile,
    context = {
        
        'room_name': 'broadcast'
    }
    return render(request, 'canecas/entregas.html',context)


@login_required
def consultar_canecas(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        form = CreateCaneca(request.POST)
        if form.is_valid():
            form.save()
            return redirect('canecas:consultas')
    else:
        form = CreateCaneca()
    #user = request.user
    canecas_user = Caneca.objects.all()
    
    context = {
        'profile': profile,
        'canecas': canecas_user,
        'form': form
    }
    return render(request, 'canecas/consultas.html',context)

@login_required
def eliminar_canecas(request, id):
    profile = request.user.profile
    caneca = get_object_or_404(Caneca, id=id)
    caneca.delete()
    context = {
        'profile': profile,
        'error': { 
                    'tipo' : 'success',
                    'titulo': 'Eliminado',
                    'texto': 'La caneca fue eliminada',
                    'tiempo': '2022'
                }
    }
    return redirect('canecas:consultas')

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def test_notification():
    print("hola ==???")
    channel_layer = get_channel_layer()
    
    print(channel_layer.group_send)
    async_to_sync(channel_layer.group_send)(
        'notification_broadcast',
        {
            "type": 'send_notification',
            "message": "Enviando notificacion"
        }
    )
    return HttpResponse("done caredone")

