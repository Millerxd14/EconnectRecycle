from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from posts.models import Post



def home(request ): # primera vista 
    
    if request.user.id != None:
        profile = request.user.profile
    else:
        profile = ""
    context = {
        'profile': profile
    }
    return render(request, 'home.html',context)