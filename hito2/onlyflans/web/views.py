from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def politicas(request):
    return render(request,'politicas.html')

def historia(request):
    return render(request,'historia.html')

def ubicacion(request):
    return render(request,'ubicacion.html')

def menu(request):
    return render(request,'menu.html')