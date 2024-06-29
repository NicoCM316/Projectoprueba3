from django.urls import path
from . import views

urlpatterns = [
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
    path('producto/', views.producto_list, name='producto_list'),
    path('producto/new/', views.producto_create, name='producto_create'),
    path('producto/<int:pk>/edit/', views.producto_update, name='producto_update'),
    path('producto/<int:pk>/delete/', views.producto_delete, name='producto_delete'),
]