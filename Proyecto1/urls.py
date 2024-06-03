from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo, despedida, damefecha, calculaEdad, views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('adios/', despedida),
    path('fecha/', damefecha),
    path('edades/<int:edad>/<int:agno>/', calculaEdad),
    path('busqueda_productos./',views.busquedaa_productos)
]
