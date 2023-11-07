from django.urls import path
from . import views

urlpatterns = [
    path('duenno/', views.DuennoLista, name="duenno"),
    path('duenno/detalle/<str:pk>', views.DuennoDetalle, name="detalle"),
    path('duenno/crear', views.DuennoCrear, name="crear"),
    path('duenno/actualizar/<str:pk>/', views.DuennoActualizar, name="actualizar"),
    path('duenno/eliminar/<str:pk>/', views.DuennoEliminar, name="eliminar"),
    path('cliente/', views.ClienteLista, name="cliente"),
    path('cliente/detalle/<str:pk>', views.ClienteDetalle, name="detalle"),
    path('cliente/crear', views.ClienteCrear, name="crear"),
    path('cliente/actualizar/<str:pk>/', views.ClienteActualizar, name="actualizar"),
    path('cliente/eliminar/<str:pk>/', views.ClienteEliminar, name="eliminar"),

]