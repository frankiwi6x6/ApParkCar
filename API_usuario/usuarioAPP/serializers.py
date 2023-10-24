from rest_framework import serializers
from .models import cliente, duenno


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class DuennoSerializer(serializers.ModelSerializer):
    class Meta:
        model = duenno
        fields = '__all__'
