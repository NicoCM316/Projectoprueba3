from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('adopta', views.adopta, name='adopta'),
    path('compras', views.compras, name='compras'),
    path('cuenta', views.cuenta, name='cuenta'),
    path('datos', views.datos, name='datos'),
    path('direcciones', views.direcciones, name='direcciones'),
    path('entrar', views.entrar, name='entrar'),
    path('misDonaciones', views.misDonaciones, name='misDonaciones'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos, name='productos'),
    path('registrarse', views.registrarse, name='registrarse'),
]