from django.contrib import messages

from .forms import AlunoForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno

def inserir_aluno(request):
    template_name = 'alunos/form_aluno.html'
    if request.method == 'POST':
        form = AlunoForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'O cadastro do aluno foi realizado com sucesso!')
        return redirect('alunos:listar_alunos')
    form = AlunoForm()
    context = {'form': form}
    return render(request, template_name, context)

def listar_alunos(request):
    template_name = 'alunos/listar_alunos.html'
    alunos = Aluno.objects.all()
    context = {'alunos': alunos}
    return render(request, template_name, context)

def editar_aluno(request, id):
    template_name = 'alunos/form_aluno.html'
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, request.FILES or None, instance=aluno)
    context = {'form': form}
    if form.is_valid():
        form.save()
        messages.success(request, 'Os dados foram atualizados com sucesso.')
        return redirect('alunos:listar_alunos')
    return render(request, template_name, context)

def excluir_aluno(request, id):
    template_name = 'alunos/excluir_aluno.html'
    aluno = Aluno.objects.get(id=id)
    context = {'aluno': aluno}
    if request.method == "POST":
        aluno.delete()
        messages.error(request, 'O Aluno foi excluído com sucesso.')
        return redirect('alunos:listar_alunos')
    return render(request, template_name, context)