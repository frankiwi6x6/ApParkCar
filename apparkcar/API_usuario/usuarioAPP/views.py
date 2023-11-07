from django.shortcuts import render
from rest_framework.response import Response
from .models import cliente, duenno
from .serializers import ClienteSerializer, DuennoSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def ClienteLista(request):
    clientes = cliente.objects.all()
    serializer = ClienteSerializer(clientes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ClienteDetalle(request, pk):
    clientes = cliente.objects.get(id=pk)
    serializer = ClienteSerializer(clientes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ClienteCrear(request):
    serializer = ClienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def ClienteActualizar(request, pk):
    clientes = cliente.objects.get(id=pk)
    serializer = ClienteSerializer(instance=clientes, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def ClienteEliminar(request, pk):
    clientes = cliente.objects.get(id=pk)
    clientes.delete()

    return Response('Eliminado')


@api_view(['GET'])
def DuennoLista(request):
    duennos = duenno.objects.all()
    serializer = DuennoSerializer(duennos, many=True)
    return Response(serializer.data)


@api_view(['GET'])  
def DuennoDetalle(request, pk):
    duennos = duenno.objects.get(id=pk)
    serializer = DuennoSerializer(duennos, many=False)
    return Response(serializer.data)


@api_view(['POST']) 
def DuennoCrear(request):
    serializer = DuennoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
def DuennoActualizar(request, pk):
    duennos = duenno.objects.get(id=pk)
    serializer = DuennoSerializer(instance=duennos, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def DuennoEliminar(request, pk):
    duennos = duenno.objects.get(id=pk)
    duennos.delete()

    return Response('Eliminado')


# Path: ApParkCar/API_calificacion/calificacionAPP/views.py
# Compare this snippet from ApParkCar/API_calificacion/calificacionAPP/views.py:
