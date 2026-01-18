from django.shortcuts import render, redirect, get_object_or_404  
from .models import Libreria, Empleado, Libro
from .forms import LibreriaForm, EmpleadoForm, LibroForm

# Create your views here.

#libreria
def listar_librerias(request):
    librerias = Libreria.objects.all()
    return render(request, 'gestionLib/listarLib.html', {'librerias': librerias})

def crear_libreria(request):
    if request.method == 'POST':
        form = LibreriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_librerias')
    else:
        form = LibreriaForm()
    return render(request, 'gestionLib/form_gener.html', {'form': form, 'titulo': 'Crear Librería'})

def editar_libreria(request, id):
    libreria = get_object_or_404(Libreria, pk=id) 
    if request.method == 'POST':
        form = LibreriaForm(request.POST, instance=libreria) 
        if form.is_valid():
            form.save()
            return redirect('listar_librerias')
    else:
        form = LibreriaForm(instance=libreria)
    return render(request, 'gestionLib/form_gener.html', {'form': form, 'titulo': 'Editar Librería'})

#empleado

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'gestionLib/listarEmp.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'gestionLib/form_gener.html', {'form': form, 'titulo': 'Registrar Empleado'})

#clase libro
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestionLib/listarLibros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'gestionLib/form_gener.html', {'form': form, 'titulo': 'Registrar Libro'})

#editar

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'gestionLib/form_gener.html', {'form': form, 'titulo': 'Editar Empleado'})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestionLib/form_gener.html', {'form': form, 'titulo': 'Editar Libro'})

#eliminar

def eliminar_libreria(request, id):
    libreria = get_object_or_404(Libreria, pk=id)
    if request.method == 'POST':
        libreria.delete()
        return redirect('listar_librerias')
    return render(request, 'gestionLib/confirmar_eliminar.html', {'objeto': libreria, 'tipo': 'la librería'})

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')
    return render(request, 'gestionLib/confirmar_eliminar.html', {'objeto': empleado, 'tipo': 'el empleado'})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'gestionLib/confirmar_eliminar.html', {'objeto': libro, 'tipo': 'el libro'})
