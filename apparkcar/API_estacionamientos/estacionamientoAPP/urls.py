from django.urls import path
from .import views
urlpatterns = [
    path('lista/', views.lista_estacionamientos, name='lista_estacionamientos'),
    path('lista/<int:id>/', views.detalle_estacionamiento_con_imagenes, name='detalle_estacionamiento'),
    path('crear/', views.crear_estacionamiento, name='crear_estacionamiento'),
    path('modifica/<int:id>/', views.modifica_estacionamiento, name='modifica_estacionamiento'),
    path('elimina/<int:id>/', views.elimina_estacionamiento, name='elimina_estacionamiento'),
    path('habilita/<int:id>/', views.habilita_estacionamiento, name='habilita_estacionamiento'),
    path('deshabilita/<int:id>/', views.deshabilita_estacionamiento, name='deshabilita_estacionamiento'),
    path('lista/<int:id>/imagenes/', views.lista_imagenes, name='lista_imagenes'),
]