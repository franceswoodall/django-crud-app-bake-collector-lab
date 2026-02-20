from .models import Bake
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def bakes_index(request): 
    bakes = Bake.objects.all()
    return render(request, 'bakes/index.html', {'bakes': bakes})

def bake_detail(request, bake_id):
    bake = Bake.objects.get(id=bake_id)
    return render(request, 'bakes/detail.html', {'bake': bake})