from django.urls import path
from .views import Dashboard
from rest_framework import routers


urlpatterns = [
    path('',Dashboard.as_view(), name='Dashboard'),
]