from .views import inicio, ver_fecha, plantilla, familia
from django.urls import path

urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path("plantilla/", plantilla),
    path("integrantes/<integrante_nombre>/<integrante_edad>", familia)
]