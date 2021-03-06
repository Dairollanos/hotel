# Generated by Django 3.1.3 on 2020-11-25 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('Tipo_Identificacion', models.CharField(choices=[('Cedula', 'Cedula'), ('Pasaporte', 'Pasaporte'), ('Otro', 'Otro')], default='Cedula', max_length=50)),
                ('Numero_Identificacion', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Estado', models.CharField(choices=[('Disponible', 'Disponible'), ('Ocupado', 'Ocupado'), ('Reservada', 'Reservada'), ('Fuera de servicio', 'Fuera de servicio')], default='Disponible', max_length=200)),
                ('Capacidad', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('Dias', models.IntegerField(default=1)),
                ('Numero_de_Personas', models.IntegerField(default=1)),
                ('Acompañantes', models.CharField(default='Ninguno', max_length=600)),
                ('precio', models.IntegerField(default=30000)),
                ('Pago', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recepcion.clientes')),
                ('Habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recepcion.habitacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fecha_pedido'],
            },
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('comentario', models.CharField(default='No comentarios', max_length=500)),
                ('Habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recepcion.habitacion')),
            ],
        ),
    ]
