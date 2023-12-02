from django.db import models

class Imagen(models.Model):
    estacionamiento = models.ForeignKey('Estacionamiento', related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes_estacionamiento/', default='default_image.jpg')

class Estacionamiento(models.Model):
    id_dueno = models.IntegerField()
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()
    precio = models.FloatField()
    capacidad = models.IntegerField()
    estado = models.BooleanField()

    def __str__(self):
        return str(self.id)