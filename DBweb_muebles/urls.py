from django.urls import path
from DBweb_muebles.views import *

urlpatterns = [
    path('', home),
    path('Sillon/', Sillon),
    path('buscar_sillones/',buscar_sillones),
    path('Mesa/', Mesa),
    path('buscar_mesas/',buscar_mesas),
    path('Armario/', Armario),
    path('buscar_armarios/',buscar_armarios),
    path('home/', home)
]

