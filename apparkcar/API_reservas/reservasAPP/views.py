from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Reserva
from .serializers import ReservaSerializer, reportesReserva

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


from django.utils import timezone

@api_view(['GET'])
def historial_reserva_estacionamiento(request, id, fechaInicio):
    ganancias = 0
    try:
        reservas = Reserva.objects.filter(id_estacionamiento=id, fecha_inicio__gte=fechaInicio).order_by('fecha_inicio')
        
        if reservas.count() == 0:
            return Response({"mensaje": "No hay reservas"}, status=404)
        else:
            result = []
            for reserva in reservas:
                fecha_actual = timezone.now()
                if reserva.fecha_fin:
                    fecha_fin = reserva.fecha_fin
                    # Calcula la diferencia de horas solo si fecha_fin no es None
                else:
                    # Si fecha_fin es None, asigna None a diferencia_horas
                    fecha_fin = fecha_actual
                diferencia_horas = round((fecha_fin - reserva.fecha_inicio).total_seconds() / 3600,0)    

                # Agregar la diferencia de horas al serializer
                precioFinal = diferencia_horas * reserva.valor
                serializer_data = reportesReserva(reserva).data
                if (reserva.fecha_fin==None):
                    serializer_data['fecha_fin'] = timezone.now()
                    serializer_data['estado'] = 'Activa'
                else:
                    serializer_data['estado'] = 'Finalizada'
                serializer_data['diferencia_horas'] = diferencia_horas
                serializer_data['precioFinal'] = precioFinal
                result.append(serializer_data)
        
            return Response(result, status=200)
        
    except Exception as e:
        return Response({"mensaje": f"Error al obtener lista de reservas - {str(e)}"}, status=500)
