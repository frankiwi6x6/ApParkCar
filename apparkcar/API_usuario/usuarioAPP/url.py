from django.urls import path
from . import views

urlpatterns = [ 
    path('verificar-credenciales/', views.verificar_credenciales, name='verificar_credenciales'),
    #Endpoints cliente
    path('cliente/', views.ClienteLista, name="cliente"),
    path('cliente/<str:pk>', views.ClienteDetalle, name="detalle"),
    path('cliente/crea/', views.ClienteCrear, name="crear"),
    path('cliente/modifica/<str:pk>', views.ClienteActualizar, name="actualizar"),
    path('cliente/elimina/<str:pk>', views.ClienteEliminar, name="eliminar"),
    #Endpoints dueño
    path('duenno/', views.DuennoLista, name="duenno"),
    path('duenno/<str:pk>', views.DuennoDetalle, name="detalle"),
    path('duenno/crea/', views.DuennoCrear, name="crear"),
    path('duenno/modifica/<str:pk>', views.DuennoActualizar, name="actualizar"),
    path('duenno/elimina/<str:pk>', views.DuennoEliminar, name="eliminar"),
    #Mostrar detalle de un usuario
    path('usuarios/', views.usuarios, name="usuarios"),
    path('usuario/<str:username>', views.UsuarioDetallePorUsuario, name="detalle_usuario"),
    path('usuario/mail/<str:email>', views.UsuarioDetallePorCorreo, name="detalle_usuario"),
    path('usuario/<str:username>/profile-pic/', views.profile_pic, name='profile_pic'),
    path('usuario/buscar/<str:username>', views.buscar_usuario, name='buscar_usuario'),
    path('default-profile-pic/', views.default_profile_pic, name='default_profile_pic'),
]
