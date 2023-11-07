from rest_framework import serializers
from .models import calificacionUsuario


class CalificacionUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = calificacionUsuario
        fields = '__all__'
