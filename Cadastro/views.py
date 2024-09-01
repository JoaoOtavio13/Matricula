from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = AlunoForms()

    else:
        form = AlunoForms()

    context = {
        'form': form
    }
    return render(request, 'cadastro/cadastro_aluno.html', context)

def litar_alunos(request):
    alunos = Aluno.objects.all()
    context={
        'alunos': alunos
    }
    return render(request, 'cadastro/listar_aluno.html',context)