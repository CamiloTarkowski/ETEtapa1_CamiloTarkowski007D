from django.db import models

# Create your models here.

class Colaborador(models.Model):
    rut = models.CharField(max_length=12,primary_key=True,verbose_name='Rut')
    nombre = models.CharField(max_length=150,verbose_name='Nombre completo')
    fono = models.IntegerField(verbose_name='Teléfono')
    direccion = models.CharField(max_length=100,verbose_name='Dirección')
    email=models.CharField(max_length=60, verbose_name='Email')
    pais=models.CharField(max_length=60,verbose_name='País')
    password=models.CharField(max_length=60, verbose_name='Contraseña')
    

    def __str__(self):
        return(self.rut)