from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import requests
from rest_framework.utils import json
from .forms import CalificacionForm, InicioSesionForm, registerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def pagina_login(request):
    form = InicioSesionForm()
    return render(request, 'web/login.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        url = 'http://18.210.214.181:8000/gestion/verificar-credenciales/'

        data = {'email': email, 'password': password}

        try:
            response = requests.post(url, data=data)

            if response.status_code == 200:
                user_data = response.json()


                return redirect('frontendAPP:index')

            else:
                mensaje_error = 'Credenciales incorrectas'
                return render(request, 'web/login.html', {'mensaje': mensaje_error, 'email': email})

        except requests.RequestException as e:
            mensaje_error = f'Error en la conexión: {e}'
            return render(request, 'web/login.html', {'mensaje': mensaje_error, 'email': email})

    else:
        return render(request, 'web/login.html')

def register(request):
    print("Entré a la función register")
    if request.method == 'POST':
        print("Recibí una solicitud POST")
        form = registerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            nombre = form.cleaned_data.get("nombre")
            ApPaterno = form.cleaned_data.get("ApPaterno")
            ApMaterno = form.cleaned_data.get("ApMaterno")
            fecha_nacimiento = form.cleaned_data.get("fecha_nacimiento").isoformat()
            password = form.cleaned_data.get("password")
            confirmar_password = form.cleaned_data.get("confirmarPassword")
            es_cliente = form.cleaned_data.get("tipo_usuario", False)

            print(f"Email: {email}")
            print(f"Nombre: {nombre}")
            print(f"Apellido Paterno: {ApPaterno}")
            print(f"Apellido Materno: {ApMaterno}")
            print(f"Fecha de nacimiento: {fecha_nacimiento}")
            print(f"Contraseña: {password}")
            print(f"Confirmar contraseña: {confirmar_password}")
            print(f"Tipo de usuario: {es_cliente}")

            if password == confirmar_password:
                data = {
                    'email': email,
                    'nombre': nombre,
                    'ApPaterno': ApPaterno,
                    'ApMaterno': ApMaterno,
                    'fecha_nacimiento': fecha_nacimiento,
                    'password': password,
                    'es_cliente': es_cliente
                }
                if es_cliente:
                    api_url = "http://18.210.214.181:8000/gestion/cliente/crea/"
                else:
                    api_url = "http://18.210.214.181:8000/gestion/duenno/crea/"

                headers = {'Content-type': 'application/json'}
                response = requests.post(api_url, data=json.dumps(data), headers=headers)

                if response.status_code ==  (200 or 201):
                    return redirect('frontendAPP:index')

        else:
            print("Formulario no válido")

    form = registerForm()
    return render(request, 'web/register.html', {'form': form})

def index(request):
    response = requests.get('http://54.146.167.224:8000/calificacion/').json()
    return render(request, 'web/index.html', {
        'response' : response
    })

def post_calificacion(request):
    url = "http://54.146.167.224:8000/calificacion/crear/"
    form = CalificacionForm(request.POST or None)
    mensaje = None

    if request.method == 'POST':
        if form.is_valid():
            id_usuario = form.cleaned_data.get("id_usuario")
            id_calificado = form.cleaned_data.get("id_calificado")
            calificacion = form.cleaned_data.get("calificacion")
            comentario = form.cleaned_data.get("comentario")
            fecha = form.cleaned_data.get("fecha").isoformat()

            if id_usuario == id_calificado:
                mensaje = 'Un usuario no puede auto calificarse.'
            else:
                data = {
                    'id_usuario': id_usuario,
                    'id_calificado': id_calificado,
                    'calificacion': calificacion,
                    'comentario': comentario,
                    'fecha': fecha
                }
                headers = {'Content-type': 'application/json'}
                response = requests.post(url, data=json.dumps(data), headers=headers)

                if response.status_code == 201:
                    mensaje = 'Calificación creada exitosamente.'
                else:
                    mensaje = f'Error al crear calificación: {response.text}'

    return render(request, 'web/index.html', {
        'response': requests.get('http://54.146.167.224:8000/calificacion/').json(),
        'form': form,
        'mensaje': mensaje,
    })
