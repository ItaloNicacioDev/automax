from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=300)
    funcao = models.CharField(max_length=100)
    idade = models.IntegerField()
    salario = models.IntegerField()

 