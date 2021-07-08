from django.urls import path
from .views import index, crear,modificar,ver_delete

urlpatterns=[
    path('',index,name="index"),
    path('crear',crear,name="crear"),
    path('ver_o_eliminar',ver_delete,name="ver_delete"),
    path('modificar',modificar,name="modificar"),
 
]