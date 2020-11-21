from django.db import models

# Create your models here.
# es como crear tablas de datos pero aqui se llaman modelos
# debes tener la mayoria de tu logica en los modulos
import string  # 
import random  # Para generar los valores random


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

# Control de la musica
class Room(models.Model):
    # Identificador del cuarto (seran caracteres)
    code = models.CharField(max_length=8, default=generate_unique_code, unique=True)
    # Quien es el dueno del cuarto
    host = models.CharField(max_length=50, unique=True)
    # Indicar si los usuarios puede pausar la musica del cuarto
    guest_can_pause = models.BooleanField(null=False, default=False)
    # 
    votes_to_skip = models.IntegerField(null=False, default=1)
    # Fecha de creacion del cuarto
    created_at = models.DateTimeField(auto_now_add=True)
