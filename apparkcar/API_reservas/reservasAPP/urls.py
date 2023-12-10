from . import views
from django.urls import path


urlpatterns = [
    path('lista/', views.lista_reservas, name='lista_reservas'),
    path('lista/<int:id>', views.detalle_reserva, name='detalle_reserva'),
    path('crea/', views.crea_reserva, name='reserva'),
    path('pago/<int:idUsuario>/<int:idEstacionamiento>', views.pago_reserva, name='pago_reserva'),
    path('modifica/<int:id>', views.modifica_reserva, name='modifica_reserva'),
    path('elimina/<int:id>', views.elimina_reserva, name='elimina_reserva'),
    path('historial/<int:id>/', views.historial_reserva, name='historial_reserva'),
    path('reporte/<int:id>/<str:fechaInicio>', views.historial_reserva_estacionamiento, name='reporte_reserva')
]