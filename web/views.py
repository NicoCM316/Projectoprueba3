from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'web/index.html', context)

def home(request):
    context={}
    return render(request, 'web/home.html', context)

def adopta(request):
    context={}
    return render(request, 'web/adopta.html', context)

def compras(request):
    context={}
    return render(request, 'web/compras.html', context)

def cuenta(request):
    context={}
    return render(request, 'web/cuenta.html', context)

def datos(request):
    context={}
    return render(request, 'web/datos.html', context)

def direcciones(request):
    context={}
    return render(request, 'web/direcciones.html', context)

def entrar(request):
    context={}
    return render(request, 'web/entrar.html', context)

def misDonaciones(request):
    context={}
    return render(request, 'web/misDonaciones.html', context)

def nosotros(request):
    context={}
    return render(request, 'web/nosotros.html', context)

def productos(request):
    context={}
    return render(request, 'web/productos.html', context)

def registrarse(request):
    context={}
    return render(request, 'web/registrarse.html', context)