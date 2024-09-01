from django.urls import path
from Cadastro.views import *

urlpatterns = [
    path('cadastro_aluno/', cadastrar_aluno, name='aluno'),
    path('listar_aluno/', litar_alunos,name='listar_aluno')
]