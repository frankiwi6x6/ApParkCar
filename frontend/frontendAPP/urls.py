from django.urls import path
from . import views

app_name = 'frontendAPP'

urlpatterns = [
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrar', views.register, name = 'register'),
    path('calificar', views.index, name='index'),
    path('form', views.post_calificacion, name='formulario')
]
