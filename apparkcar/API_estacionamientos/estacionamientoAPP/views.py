import os
import uuid
from django.shortcuts import render
from django.http import JsonResponse
from .models import Estacionamiento, Imagen
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response
from django.db.models import F, ExpressionWrapper, FloatField
from django.db.models.expressions import ExpressionWrapper
from django.db.models.functions import ACos, Cos, Radians, Sin

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
def lista_estacionamientos_duenno(request, id):
    estacionamientos = Estacionamiento.objects.filter(id_dueno=id)
    if estacionamientos.count() == 0:
        return Response({"detail": "No hay estacionamientos registrados"}, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = EstacionamientoSerializer(estacionamientos, many=True)
        
    return Response(serializer.data)


@api_view(['GET'])
def detalle_estacionamiento_con_imagenes(request, id):
    estacionamiento = get_object_or_404(Estacionamiento, pk=id)
    est_serializer = EstacionamientoSerializer(estacionamiento)
    imagenes = estacionamiento.imagenes.all()
    imagenes_serializer = ImagenSerializer(imagenes, many=True)
    
    serializer = {'estacionamiento': est_serializer.data, 'url': imagenes_serializer.data}
    print(imagenes_serializer.data)
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


@api_view(['GET'])
def get_estacionamientos_ordenados_por_distancia(request, latitud_usuario, longitud_usuario):
    # Convertir los parámetros de la URL a valores numéricos
    latitud_usuario = float(latitud_usuario)
    longitud_usuario = float(longitud_usuario)

    # Calcular la distancia usando la fórmula haversine
    estacionamientos = Estacionamiento.objects.annotate(
        distancia=ExpressionWrapper(
            ACos(
                Cos(Radians(latitud_usuario)) *
                Cos(Radians(F('latitud'))) *
                Cos(Radians(F('longitud')) - Radians(longitud_usuario)) +
                Sin(Radians(latitud_usuario)) * Sin(Radians(F('latitud')))
            ) * 6371,  # Radio de la Tierra en kilómetros
            output_field=FloatField()
        )
    )

    # Ordenar los estacionamientos por distancia
    estacionamientos_ordenados = estacionamientos.order_by('distancia')

    # Convertir los resultados a un formato adecuado (por ejemplo, JSON)
    resultados = [
        {
            'id': estacionamiento.id,
            'titulo': estacionamiento.titulo,
            'descripcion': estacionamiento.descripcion,
            'tipo': estacionamiento.tipo,
            'precio' : estacionamiento.precio,
            'capacidad' : estacionamiento.capacidad,
            'latitud': estacionamiento.latitud,
            'longitud': estacionamiento.longitud,
            'distancia': round(estacionamiento.distancia,2)
            # Agrega otros campos según sea necesario
        }
        for estacionamiento in estacionamientos_ordenados
    ]

    return JsonResponse(resultados, safe=False)