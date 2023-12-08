import uuid
from django.contrib.auth.models import User
from django.db import models
import os


def generate_filename(instance, filename):
    filename = f"{instance.username}_profile-pic.png"
    return os.path.join('profile_pics', filename)

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50, default='DEFAULT VALUE')
    ApPaterno = models.CharField(max_length=50, default='DEFAULT VALUE')
    ApMaterno = models.CharField(max_length=50, default='DEFAULT VALUE')
    fecha_nacimiento = models.DateField()
    es_cliente = models.BooleanField(default=True)
    password = models.CharField(max_length=50, default='password')
    profile_pic = models.ImageField(upload_to=generate_filename, blank=True, default='profile_pics/default.png')
    def profile_pic_url(self):
        return f'http://127.0.0.1:8000/gestion/usuario/{self.username}/profile-pic/'
        
    def __str__(self):
        return self.email