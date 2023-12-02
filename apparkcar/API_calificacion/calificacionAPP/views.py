from django.shortcuts import render
from rest_framework.response import Response
from .models import calificacionUsuario
from .serializers import CalificacionUsuariosSerializer
from rest_framework.decorators import api_view
from django.db.models import Avg

from django.http import JsonResponse, HttpResponse
# Create your views here.


@api_view(['GET'])
def CalificacionUsuariosLista(request):
    calificacionusuarios = calificacionUsuario.objects.all()
    serializer = CalificacionUsuariosSerializer(calificacionusuarios, many=True)
    return Response(serializer.data)
    


@api_view(['GET'])
def CalificacionUsuariosDetalle(request, pk):
    calificacionusuarios = calificacionUsuario.objects.get(id_calificacion=pk)
    serializer = CalificacionUsuariosSerializer(calificacionusuarios, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def CalificacionUsuariosActualizar(request, pk):
    calificacionusuarios = calificacionUsuario.objects.get(id=pk)
    serializer = CalificacionUsuariosSerializer(instance=calificacionusuarios, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def CalificacionUsuariosEliminar(request, pk):
    calificacionusuarios = calificacionUsuario.objects.get(id=pk)
    calificacionusuarios.delete()

    return Response('Eliminado')

@api_view(['POST'])
def CalificacionUsuariosCrear(request):
    serializer = CalificacionUsuariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

def obtenerCalificacionUsuario(request, pk):
    try:
        pk = int(pk)
    except ValueError:
        return JsonResponse({'error': 'El ID de usuario debe ser un número entero'}, status=400)

    try:
        lista_calificaciones = calificacionUsuario.objects.filter(id_calificado=pk)
        promedio_calificaciones = calificacionUsuario.objects.filter(id_calificado=pk).aggregate(Avg('calificacion'))
        promedio_calificacion = round(promedio_calificaciones['calificacion__avg'], 2)
        serializer = CalificacionUsuariosSerializer(lista_calificaciones, many=True)
        return JsonResponse({'calificaciones': serializer.data, 'promedio_calificacion': promedio_calificacion})

    except calificacionUsuario.DoesNotExist:
        return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

    except Exception as e:
        return JsonResponse({'error': f'Error en la solicitud: {str(e)}'}, status=500)