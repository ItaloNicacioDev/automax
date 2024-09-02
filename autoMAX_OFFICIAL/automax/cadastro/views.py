from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FuncionariosForm 

# Create your views here.
def cadastro_func(request):
    return render(request, 'home.html')

#criar form do cadastro
def cadastrar_func(request):
    if request.method == 'POST':
        form = FuncionariosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Funcionário cadastrado com sucesso!")  # Testando a resposta
    else:
        form = FuncionariosForm()

    return render(request, 'home.html', {'form': form})


