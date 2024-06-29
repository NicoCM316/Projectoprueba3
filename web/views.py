from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from .forms import ProductoForm


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


# Crear Producto
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'web/producto_form.html', {'form': form})

# Listar Productos
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'web/producto_list.html', {'productos': productos})

# Actualizar Producto
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'web/producto_form.html', {'form': form})

# Eliminar Producto
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'web/producto_delete.html', {'producto': producto})
