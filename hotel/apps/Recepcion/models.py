from django.db import models
from django.contrib.auth.models import User


class Habitacion(models.Model):
    dsp = 'Disponible'
    estados = [
        ('Disponible','Disponible'),
        ('Ocupado','Ocupado'),
        ('Reservada','Reservada'),
        ('Fuera de servicio','Fuera de servicio')]
    Nombre = models.CharField(max_length=200)
    Estado = models.CharField(choices=estados, default=dsp, max_length=200)
    Capacidad = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Nombre


class Clientes(models.Model):
    idnt = 'Cedula'
    tipos = [
        ('Cedula', 'Cedula'),
        ('Pasaporte', 'Pasaporte'),
        ('Otro', 'Otro')]
    Tipo_Identificacion = models.CharField(choices=tipos, default=idnt, max_length=50)
    Numero_Identificacion = models.CharField(primary_key=True, max_length=200)
    Nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.Nombre


class Reservas(models.Model):
    Nombre = models.CharField(max_length=200)
    Habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    comentario = models.CharField(default='No comentarios', max_length=500)

    def __str__(self):
        return self.Nombre


class Servicio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    Cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    Habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    Dias = models.IntegerField(default=1)
    Numero_de_Personas = models.IntegerField(default=1)
    Acompañantes = models.CharField(default='Ninguno', max_length=600)
    precio = models.IntegerField(default=30000)
    Pago = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    comentario = models.CharField(blank=True, null=True, max_length=500)

    class Meta:
        ordering = ['-fecha_pedido']

    def __str__(self):
        return str(self.fecha_pedido)
