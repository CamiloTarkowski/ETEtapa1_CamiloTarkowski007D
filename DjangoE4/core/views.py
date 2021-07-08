from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm
from django.views.decorators import csrf
from rest_framework.serializers import Serializer


def index (request):

    return render(request,'index.html')

def crear(request):
    if request.method=='POST': 
        colaborador_form = ColaboradorForm(request.POST)
        if colaborador_form.is_valid():
            colaborador_form.save()
            return redirect('index.html')
    else:
        colaborador_form = ColaboradorForm()
    return render(request, 'core/crear.html', {'colaborador_form': colaborador_form})

def ver_delete (request):

    return render(request,'core/ver_delete.html')

def modificar (request):

    return render(request,'core/modificar.html')
