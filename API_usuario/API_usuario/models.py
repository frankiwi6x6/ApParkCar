from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class cliente(models.Model):
    nombre = models.CharField(max_length=50, default='DEFAULT VALUE')
    email = models.CharField(max_length=100, default='DEFAULT VALUE')
    ApPaterno = models.CharField(max_length=50, default='DEFAULT VALUE')
    ApMaterno = models.CharField(max_length=50, default='DEFAULT VALUE')
    password = models.CharField(max_length=100, default='DEFAULT VALUE')
    fecha_nacimiento = models.DateField()
    id_cliente = models.AutoField(primary_key=True)



    class Meta:
        db_table = 'clientes'

    #def __str__(self):
    #    return self.nombre

class duenno(models.Model):
    nombre = models.CharField(max_length=50, default='DEFAULT VALUE')
    email = models.CharField(max_length=100, default='DEFAULT VALUE')
    ApPaterno = models.CharField(max_length=50, default='DEFAULT VALUE')
    ApMaterno = models.CharField(max_length=50, default='DEFAULT VALUE')
    password = models.CharField(max_length=100, default='DEFAULT VALUE')
    fecha_nacimiento = models.DateField()
    id_duenno = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'duennos'

    #def __str__(self):
    #    return self.nombre