from django.urls import path
from .import views

urlpatterns = [
    path('', views.CalificacionUsuariosLista, name="calificaciones"),
    path('detalle/<str:pk>', views.CalificacionUsuariosDetalle, name="detalle"),
    path('crear', views.CalificacionUsuariosCrear, name="crear"),
    path('actualizar/<str:pk>/', views.CalificacionUsuariosActualizar, name="actualizar"),
    path('eliminar/<str:pk>/', views.CalificacionUsuariosEliminar, name="eliminar"),
]