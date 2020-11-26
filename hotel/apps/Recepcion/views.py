from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *


class Dashboard(generics.ListCreateAPIView):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer