import os
import uuid
from django.shortcuts import render
from django.http import JsonResponse
from .models import Estacionamiento, Imagen
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response

from .serializers import EstacionamientoSerializer, ImagenSerializer

@api_view(['POST'])
def crear_estacionamiento(request):
    if request.method == 'POST':
        data = request.data
        imagenes = request.FILES.getlist('imagenes')

        estacionamiento_serializer = EstacionamientoSerializer(data=data)
        if estacionamiento_serializer.is_valid():
            estacionamiento = estacionamiento_serializer.save()

            for imagen in imagenes:
                # Genera un nombre único para cada imagen
                nombre_uniq = str(uuid.uuid4())
                # Construye la ruta del archivo en el servidor
                ruta_archivo = os.path.join('imagenes_estacionamiento', f'{nombre_uniq}.jpg')
                with open(ruta_archivo, 'wb') as f:
                    for chunk in imagen.chunks():
                        f.write(chunk)
                # Crea el objeto de imagen y guarda la URL en la base de datos
                Imagen.objects.create(estacionamiento=estacionamiento, imagen=f'/{ruta_archivo}')

            return JsonResponse(estacionamiento_serializer.data, status=201)
        return JsonResponse(estacionamiento_serializer.errors, status=400)

@api_view(['GET'])
def lista_estacionamientos(request, id=None):
    if id is not None:
        estacionamiento = get_object_or_404(Estacionamiento, pk=id)

        serializer = EstacionamientoSerializer(estacionamiento)
        return Response(serializer.data)
    else:
        estacionamientos = Estacionamiento.objects.all()
        serializer = EstacionamientoSerializer(estacionamientos, many=True)

        return Response(serializer.data)


@api_view(['GET'])
def detalle_estacionamiento_con_imagenes(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, pk=id)
    est_serializer = EstacionamientoSerializer(estacionamiento)
    imagenes = estacionamiento.imagenes.all()
    imagenes_serializer = ImagenSerializer(imagenes, many=True)
    serializer = {'estacionamiento': est_serializer.data, 'url': imagenes_serializer.data}

    return Response(serializer)

@api_view(['PUT'])
def modifica_estacionamiento(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, pk=id)
    serializer = EstacionamientoSerializer(estacionamiento, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def elimina_estacionamiento(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, pk=id)
    estacionamiento.delete()
    return Response({"message": "Estacionamiento eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def habilita_estacionamiento(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, pk=id)
    estacionamiento.estado = not estacionamiento.estado  # Cambia el estado a habilitado o deshabilitado
    estacionamiento.save()
    return Response({"message": f"Estado de estacionamiento modificado a {'habilitado' if estacionamiento.estado else 'deshabilitado'}"})

@api_view(['GET'])
def deshabilita_estacionamiento(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, pk=id)
    estacionamiento.estado = False
    estacionamiento.save()
    return Response({"message": "Estacionamiento deshabilitado correctamente"})



@api_view(['GET'])
def lista_imagenes(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, pk=id)
    imagenes = estacionamiento.imagenes.all()
    serializer = ImagenSerializer(imagenes, many=True)

    return Response(serializer.data)