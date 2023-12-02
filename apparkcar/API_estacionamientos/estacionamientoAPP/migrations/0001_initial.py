# Generated by Django 3.2.3 on 2023-11-25 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dueno', models.IntegerField()),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('precio', models.FloatField()),
                ('capacidad', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('estacionamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='estacionamientoAPP.estacionamiento')),
            ],
        ),
    ]
