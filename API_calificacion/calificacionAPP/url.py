from django.urls import path
from .import views

urlpatterns = [
    path('', views.CalificacionUsuariosLista, name="calificaciones"),
    path('<str:pk>', views.CalificacionUsuariosDetalle, name="detalle"),
    path('', views.CalificacionUsuariosCrear, name="crear"),
    path('<str:pk>', views.CalificacionUsuariosActualizar, name="actualizar"),
    path('<str:pk>', views.CalificacionUsuariosEliminar, name="eliminar"),
]
