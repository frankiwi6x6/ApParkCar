from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests
# Create your views here.

@api_view(['GET'])
def reportePagos(request, idDuenno, fechaInicio):
    if request.method == 'GET':
        URL_ESTACIONAMIENTOS = f'http://3.91.111.224:8002/estacionamientos/duenno/{idDuenno}/'

        IP_RESERVAS = '3.91.111.224'
        estacionamientos = requests.get(URL_ESTACIONAMIENTOS)
        print(estacionamientos)
        allBooking = []
        lessUsedParking = []
        ganancias = 0
        
        if estacionamientos.status_code != 404:
            for estacionamiento in estacionamientos.json():
                URL_RESERVAS = f'http://{IP_RESERVAS}:8003/reserva/reporte/{estacionamiento["id"]}/{fechaInicio}'
                
                try:
                    estacionamientos.json().sort(key=lambda x: x['id'])
                    booking = requests.get(URL_RESERVAS)
                    booking_json = booking.json()
                    
                    if booking.status_code == 404:
                        lessUsedParking.append(estacionamiento["id"])
                    else:
                        for reserva in booking_json:
                            ganancias += reserva["precioFinal"]
                            fechaActual = reserva["fecha_fin"]
                        allBooking.append(booking_json)
                except requests.exceptions.RequestException as e:
                    print(f"Error al obtener reservas de {URL_RESERVAS}: {e}")

            return JsonResponse({"reservas": allBooking, "estacionamientosMenosUsados": lessUsedParking, "ganancias": ganancias, "mensaje": f"Calculo realizado para la fecha: {fechaActual}"}, safe=False)
        else:
            return JsonResponse({"mensaje": "El usuario ingresado no es de tipo dueño o no tiene estacionamientos listados"}, status=404)

