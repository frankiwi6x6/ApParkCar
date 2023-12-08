from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reserva
from .serializers import ReservaSerializer

@api_view(['GET'])
def lista_reservas(request):
    try:
        reservas = Reserva.objects.all()
        
        if reservas.count() == 0:
            return Response({"mensaje": "No hay reservas"}, status=404)
        else:
            serializer = ReservaSerializer(reservas, many=True)
            return Response(serializer.data, status=200)
        
    except Exception as e:
        return Response({"mensaje": f"Error al obtener lista de reservas - {str(e)}"}, status=500)

@api_view(['GET'])
def detalle_reserva(request, id):
    try:
        reserva = get_object_or_404(Reserva, id=id)
        serializer = ReservaSerializer(reserva, many=False)

        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"mensaje": f"Error al obtener reserva - {str(e)}"}, status=500)

@api_view(['GET'])
def pago_reserva(request, idUsuario, idEstacionamiento):
    try:
        reserva = Reserva.objects.filter(id_usuario=idUsuario, id_estacionamiento=idEstacionamiento).order_by('-id')[0]
        serializer = ReservaSerializer(reserva, many=False)

        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"mensaje": f"Error al obtener reserva de pago - {str(e)}"}, status=500)

@api_view(['POST'])
def crea_reserva(request):
    # Aquí debes implementar la lógica para crear una nueva reserva
    
    try:
       if request.method == 'POST':
            data = request.data
            reserva_serializer = ReservaSerializer(data=data)
            if reserva_serializer.is_valid():
                reserva = reserva_serializer.save()
                return Response(reserva_serializer.data, status=201)
            return Response(reserva_serializer.errors, status=400)
          
    except Exception as e:
        return Response({"mensaje": f"Error al crear reserva - {str(e)}"}, status=500)
    
    

@api_view(['PUT'])
def modifica_reserva(request):
    # Aquí debes implementar la lógica para modificar una reserva existente
    return Response({"mensaje": "Modifica reserva"}, status=200)

@api_view(['DELETE'])
def elimina_reserva(request, id):
    # Aquí debes implementar la lógica para eliminar una reserva existente
    return Response({"mensaje": "Reserva eliminada exitosamente"}, status=204)

@api_view(['GET'])
def historial_reserva(request, id):
    try:
        reservas = Reserva.objects.filter(id_usuario=id).order_by('fecha_inicio')
        
        if reservas.count() == 0:
            return Response({"mensaje": "No hay reservas"}, status=404)
        else:
            serializer = ReservaSerializer(reservas, many=True)
            return Response(serializer.data, status=200)
        
    except Exception as e:
        return Response({"mensaje": f"Error al obtener lista de reservas - {str(e)}"}, status=500)
