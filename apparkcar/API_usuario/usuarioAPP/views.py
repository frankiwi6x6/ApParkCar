from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import binascii
from django.contrib.staticfiles import finders
import datetime as dt

# Create your views here.

@csrf_exempt
@require_POST
def verificar_credenciales(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        print(f"Intentando autenticar con correo electrónico: {email}")

        # Intenta obtener al usuario por su correo electrónico
        usuario = Usuario.objects.get(email=email)
        contrasenaDB = usuario.password
        print(f"Usuario encontrado: {usuario}")


        if password ==  contrasenaDB:
            # Las credenciales son válidas
            print("Credenciales válidas")
            return JsonResponse({'mensaje': 'Credenciales válidas'}, status=200)
           
        else:
            # Las credenciales no son válidas
            print("Credenciales incorrectas")
            return JsonResponse({'mensaje': 'Credenciales incorrectas'}, status=401)

    except Usuario.DoesNotExist:
        # El usuario no existe
        print("Usuario no encontrado")
        return JsonResponse({'mensaje': 'Credenciales incorrectas'}, status=401)

# Endpoints CLIENTE
@api_view(['GET'])
def ClienteLista(request):
    clientes = Usuario.objects.filter(es_cliente=True)
    serializer = UsuarioSerializer(clientes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ClienteDetalle(request, pk):
    cliente = get_object_or_404(Usuario, id=pk, es_cliente=True)
    serializer = UsuarioSerializer(cliente, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def ClienteCrear(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    #Generar calificación vacía hacia la API mediante POST:
    URL_CALIFICACIONES = 'http://3.91.111.224:8001/calificacion/crear/'
    data = {
        "id_usuario": -1,
        "id_calificado": serializer.data['id'],
        "calificacion": 0,
        "comentario": "Usuario creado",
        "fecha": dt.now()}
    requests.post(URL_CALIFICACIONES, data=data)
    return Response(serializer.data)


@api_view(['POST'])
def ClienteActualizar(request, pk):
    clientes = Usuario.objects.get(id=pk)
    serializer = UsuarioSerializer(instance=clientes, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def ClienteEliminar(request, pk):
    clientes = Usuario.objects.get(id=pk)
    clientes.delete()

    return Response('Eliminado')


@api_view(['GET'])
def DuennoLista(request):
    duennos = Usuario.objects.filter(es_cliente=False)
    serializer = UsuarioSerializer(duennos, many=True)
    
    return Response(serializer.data)


@api_view(['GET'])  
def DuennoDetalle(request, pk):
    duenno = get_object_or_404(Usuario, id=pk, es_cliente=False)
    serializer = UsuarioSerializer(duenno, many=False)
    return Response(serializer.data)

@api_view(['POST']) 
def DuennoCrear(request):
    
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        
        
        
    else:
        return Response(serializer.errors)

    #Generar calificación vacía hacia la API mediante POST:
    URL_CALIFICACIONES = 'http://3.91.111.224:8001/calificacion/crear/'
    data = {
        "id_usuario": -1,
        "id_calificado": serializer.data['id'],
        "calificacion": 0,
        "comentario": "Usuario creado",
        "fecha": dt.now()}
    requests.post(URL_CALIFICACIONES, data=data)
    return Response(serializer.data)

        



@api_view(['POST'])
def DuennoActualizar(request, pk):
    duennos = Duenno.objects.get(id=pk)
    serializer = DuennoSerializer(instance=duennos, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def DuennoEliminar(request, pk):
    duennos = Duenno.objects.get(id=pk)
    duennos.delete()

    return Response('Eliminado')

@api_view(['GET'])
def UsuarioDetallePorUsuario(request, username):
    usuario = get_object_or_404(Usuario, username=username)
    serializer = UsuarioSerializer(usuario, many=False)

    # Incluir la URL de la foto del perfil en la respuesta JSON
    data = serializer.data
    data['profile_pic_url'] = f'http:///3.91.111.224:8000/gestion/usuario/{username}/profile-pic/'

    return JsonResponse(data, status=200)

@api_view(['GET'])
def UsuarioDetallePorCorreo(request, email):
    usuario = get_object_or_404(Usuario, email=email)
    serializer = UsuarioSerializer(usuario, many=False)
    return Response(serializer.data)


def profile_pic(request, username):
    user = get_object_or_404(Usuario, username=username)
    image_path = user.profile_pic.path

    with open(image_path, 'rb') as image_file:
        response = HttpResponse(image_file.read(), content_type='image/png')

    return response

def default_profile_pic(request):
    default_image_path = 'media/profile_pics/default.png'

    with open(default_image_path, 'rb') as image_file:
        image_data = image_file.read()

    return HttpResponse(image_data, content_type='image/png')

@api_view(['GET'])
def usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    
    return JsonResponse(serializer.data,status=200)

@api_view(['GET'])
def buscar_usuario(request, username):
    usuarios = Usuario.objects.filter(username__startswith=username)

    if not usuarios.exists():
        return JsonResponse({'message': 'No se han encontrado usuarios'}, status=404)

    serializer = UsuarioSerializer(usuarios, many=True)

    # Modificar la respuesta JSON para incluir la URL de la foto del perfil
    data = serializer.data
    for user_data in data:
        user_data['profile_pic_url'] = f'http:///3.91.111.224:8000/gestion/usuario/{user_data["username"]}/profile-pic/'

    return JsonResponse(data, safe=False)

# Path: ApParkCar/API_calificacion/calificacionAPP/views.py
# Compare this snippet from ApParkCar/API_calificacion/calificacionAPP/views.py:
