from django.shortcuts import render
from rest_framework.response import Response
from .models import calificacionUsuario
from .serializers import CalificacionUsuariosSerializer
from rest_framework.decorators import api_view

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


