from django.db import models
# Create your models here.
class Libreria(models.Model):
    nombre_libreria = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la libreria")
    direccion_lib = models.CharField(max_length=200, verbose_name="Dirección")
    numero_estantes = models.IntegerField(verbose_name="numero de estantes")

    def __str__(self):
        return self.nombre_libreria
    
class Empleado(models.Model):
    nombre_completo = models.CharField(max_length = 200)
    cargo_empleado = models.CharField (max_length=100, help_text= "Ejemp: Vendedor, Cajero")
    salario_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    libreria = models.ForeignKey(Libreria, on_delete=models.CASCADE, related_name="empleados")

    def __str__(self):
        return self.nombre_completo
    
class Libro(models.Model):
    titulo_libro = models.CharField(max_length=200)
    autor_principal = models.CharField(max_length=200)
    genero_lit = models.CharField(max_length=200)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    numero_paginas = models.IntegerField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,verbose_name="registrado por")

    def __str__(self):
        return self.titulo_libro


    
    

