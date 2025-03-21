from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')  # O caminho dentro de 'templates'

def usuarios(request):
    if request.method == "POST":
        novo_usuario = Usuario(
            nome=request.POST.get('nome'),
            idade=request.POST.get('idade')
        )
        novo_usuario.save()

    usuarios = Usuario.objects.all()  # Corrigindo a passagem de dados
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})


def listagem_usuarios(request):
    usuarios = Usuario.objects.all()  # Buscar todos os usuários
    return render(request, 'usuarios/listagem.html', {'usuarios': usuarios})

