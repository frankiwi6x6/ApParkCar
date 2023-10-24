from django.db import models

# Create your models here.

class calificacionUsuario(models.Model):

    id_calificacion = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_calificado = models.IntegerField()
    calificacion = models.IntegerField()
    comentario = models.CharField(max_length=100, default='DEFAULT VALUE')
    fecha = models.DateField()

    class Meta:
        db_table = 'calificacion'
    
    def __str__(self):
       return self.nombre

