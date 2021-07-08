from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Colaborador


class ColaboradorForm(forms.ModelForm):

    class Meta: 
        model= Colaborador
        fields = ['rut', 'nombre', 'fono', 'direccion', 'email','pais', 'password', ]
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre completo', 
            'fono': 'Teléfono',
            'direccion': 'Dirección', 
            'email': 'Email',
            'pais':'País', 
            'password': 'Contraseña', 
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre completo', 
                    'id': 'nombre'
                }
            ), 
            
            'fono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese teléfono', 
                    'id': 'fono',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese dirección', 
                    'id': 'direccion',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese email', 
                    'id': 'email',
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese país', 
                    'id': 'pais',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese contraseña', 
                    'id': 'password',
                }
            )


        }