from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recepcion/', include('apps.Recepcion.urls')),
    #path('usuario/', include('apps.Usuarios.urls'))
]
