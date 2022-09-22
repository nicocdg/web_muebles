from django.shortcuts import render
from django.http import HttpResponse
from DBweb_muebles.models import *

def home(request):
    return render(request,"home.html")

def Armario(request):
    if request.method == "POST":
        armario = Armarios(modelo=request.POST['modelo'], material=request.POST['material'],puertas=request.POST['puertas'])
        armario.save()
        return render(request, "home.html") #nos lleva a home
    return render(request, "Armarios.html")

def buscar_armarios(request):
    if request.GET['modelo']:
        modelo = request.GET['modelo']
        armario = Armarios.objects.filter(modelo__icontains= modelo)
        return render(request, "Armarios.html", {'armario_busqueda': armario}) 
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)

def Mesa(request):
    if request.method == "POST":
        mesa = Mesas(modelo=request.POST['modelo'], material=request.POST['material'],capacidadPersonas=request.POST['capacidadPersonas'])
        mesa.save()
        return render(request, "home.html") #nos lleva a home
    return render(request, "Mesas.html")

def buscar_mesas(request):
    if request.GET['modelo']:
        modelo = request.GET['modelo']
        mesa = Mesas.objects.filter(modelo__icontains= modelo)
        return render(request, "Mesas.html", {'mesa_busqueda': mesa}) 
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)

def Sillon(request):
    if request.method == "POST":
        sillon = Sillones(modelo=request.POST['modelo'], material=request.POST['material'],cuerpos=request.POST['cuerpos'])
        sillon.save()
        return render(request, "home.html") #nos lleva a home
    return render(request, "Sillones.html")

def buscar_sillones(request):
    if request.GET['modelo']:
        modelo = request.GET['modelo']
        sillon = Sillones.objects.filter(modelo__icontains= modelo)
        return render(request, "Sillones.html", {'sillon_busqueda': sillon}) 
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)
