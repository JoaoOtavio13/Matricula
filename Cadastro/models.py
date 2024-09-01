from django.db import models

# Create your models here.
Lista_Cidades=[
    ('São Miguel','São Miguel'),
    ('Pau dos Ferros','Pau dos Ferros'),
]

Lista_Cursos=[
    ('Informática','Informática'),
    ('Alimentos','Alimentos'),
    ('Apicultura','Apicultura'),
]

class Aluno(models.Model):
    nome=models.CharField(max_length=200)
    endereco=models.CharField(max_length=200)
    cidade=models.CharField(max_length=200,choices=Lista_Cidades)
    email=models.EmailField()
    curso=models.CharField(max_length=200,choices=Lista_Cursos)
    