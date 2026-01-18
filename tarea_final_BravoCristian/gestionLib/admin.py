from django.contrib import admin
from .models import Libreria, Empleado, Libro

# Register your models here.
@admin.register(Libreria)
class LibreriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_libreria', 'direccion_lib', 'numero_estantes')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cargo_empleado', 'libreria')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo_libro', 'autor_principal', 'precio_venta', 'empleado')