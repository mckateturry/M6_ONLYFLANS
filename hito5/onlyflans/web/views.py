from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Flan, Cafe, ContactForm
from .forms import ContactoFormForm
from django.contrib.auth.decorators import login_required

def index(request):
    flanes = Flan.objects.filter(is_private=False) 
    return render(request,'index.html',{'flanes': flanes})

@login_required #SE HABILITA QUE CON LA VISTA SE PUEDA INGRESAR CON LOGIN
def bienvenido(request):
    flanes = Flan.objects.filter(is_private=True) 
    return render(request,'bienvenido.html',{'flanes': flanes})

def menu(request):
    cafes = Cafe.objects.filter(is_private=False) 
    return render(request,'menu.html',{'cafes': cafes})

def politicas(request):
    return render(request,'politicas.html')

def historia(request):
    return render(request,'historia.html')

def ubicacion(request):
    return render(request,'ubicacion.html')

def menualternativo(request):
    return render(request,'menualternativo.html')

def contacto(request):
    if request.method == 'POST':
            form = ContactoFormForm(request.POST)
            if form.is_valid():
                contact_form = ContactForm.objects.create(**form.cleaned_data)
                return HttpResponseRedirect('/exito')
        
    else:
            form = ContactoFormForm()
    
    return render(request,'contacto.html',{'form': form})
    
def exito(request):
    return render(request,'exito.html')