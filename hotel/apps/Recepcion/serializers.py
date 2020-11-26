from rest_framework import serializers
from .models import *


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['Nombre', 'Estado', 'Capacidad']