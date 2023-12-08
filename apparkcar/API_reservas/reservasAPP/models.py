from django.db import models

# Create your models here.

class Reserva(models.Model):
    ACEPTADA = 'A'
    RECHAZADA = 'R'
    PENDIENTE = 'P'
    CANCELADA = 'C'
    ESTADO_RESERVA = [
        (ACEPTADA, 'Aceptada'),
        (RECHAZADA, 'Rechazada'),
        (PENDIENTE, 'Pendiente'),
        (CANCELADA, 'Cancelada'),
    ]



    id = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField(null=False, blank=False)
    id_estacionamiento = models.IntegerField(null=False, blank=False)
    fecha_inicio = models.DateTimeField(null=False, blank=False)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_RESERVA,
        default=PENDIENTE,
    )
    valor = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Reserva {self.id} - Usuario {self.id_usuario} - Estacionamiento {self.id_estacionamiento} - Estado {self.estado}"
