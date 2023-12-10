from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        
class reportesReserva(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('id_estacionamiento', 'fecha_inicio', 'fecha_fin' ,'valor')
        

