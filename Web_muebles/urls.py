from django.contrib import admin
from django.urls import path, include
from Web_muebles.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sillonesFromDB/', sillonesFromDB),
    path('mesasFromDB/', mesasFromDB),
    path('armariosFromDB/', armariosFromDB),
    path('addMuebles/', addMuebles),
    path('DBweb_muebles/', include("DBweb_muebles.urls")),

]
