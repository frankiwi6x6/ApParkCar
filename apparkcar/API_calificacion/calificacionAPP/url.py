from django.urls import path
from .import views

urlpatterns = [
    path('', views.CalificacionUsuariosLista, name="calificaciones"),
    path('<str:pk>', views.CalificacionUsuariosDetalle, name="detalle"),
    path('crear/', views.CalificacionUsuariosCrear, name="crear"),
    path('<str:pk>', views.CalificacionUsuariosActualizar, name="actualizar"),
    path('<str:pk>', views.CalificacionUsuariosEliminar, name="eliminar"),
    path('calificaciones/<str:pk>', views.obtenerCalificacionUsuario, name="obtenerCalificacionUsuario"),
    path('<str:from_user>/<str:to_user>', views.obtenerCalificacion, name='obtenerCalificacion'),
    path('modificar/<str:from_user>/<str:to_user>/<str:calificacion>', views.actualizarCalificacion, name='actualizarCalificacion')
]
