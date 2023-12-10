from . import views
from django.urls import path
urlpatterns = [
    path('reporte/<int:idDuenno>/<str:fechaInicio>', views.reportePagos, name='reportePagos'),
] 
