# Generated by Django 3.2.3 on 2023-12-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservasAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='comentario',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(choices=[('A', 'Aceptada'), ('R', 'Rechazada'), ('P', 'Pendiente'), ('C', 'Cancelada')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='valor',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
