# Generated by Django 3.2.3 on 2023-11-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarioAPP', '0005_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
