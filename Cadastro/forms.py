from django import forms
from .models import *

class AlunoForms(forms.ModelForm):
    class Meta:
        model= Aluno
        fields= '__all__'

        widgets={
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }