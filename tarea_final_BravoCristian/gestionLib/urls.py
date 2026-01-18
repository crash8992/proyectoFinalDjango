from django.urls import path
from . import views

urlpatterns = [
    # Libreria
    path('', views.listar_librerias, name='listar_librerias'),
    path('libreria/crear/', views.crear_libreria, name='crear_libreria'),
    path('libreria/editar/<int:id>/', views.editar_libreria, name='editar_libreria'),
    
    # Empleados
    path('empleados/', views.listar_empleados, name='listar_empleados'),
    path('empleados/crear/', views.crear_empleado, name='crear_empleado'),

    # Libros
    path('libros/', views.listar_libros, name='listar_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),

    #editar
    path('empleados/editar/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('libros/editar/<int:id>/', views.editar_libro, name='editar_libro'),
    
    #eliminar
    path('libreria/eliminar/<int:id>/', views.eliminar_libreria, name='eliminar_libreria'),
    path('empleados/eliminar/<int:id>/', views.eliminar_empleado, name='eliminar_empleado'),
    path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]
