from django import forms
from .models import Libreria, Empleado, Libro

class LibreriaForm(forms.ModelForm):
    class Meta:
        model = Libreria
        fields = '__all__' 
        widgets = {
            'nombre_libreria': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_lib': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_estantes': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo_empleado': forms.TextInput(attrs={'class': 'form-control'}),
            'salario_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
            'libreria': forms.Select(attrs={'class': 'form-control'}),
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'titulo_libro': forms.TextInput(attrs={'class': 'form-control'}),
            'autor_principal': forms.TextInput(attrs={'class': 'form-control'}),
            'genero_lit': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'numero_paginas': forms.NumberInput(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
        }