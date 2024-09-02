from django import forms
from .models import Funcionarios
from django.shortcuts import render, redirect

class FuncionariosForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'sobrenome', 'funcao', 'idade', 'salario']