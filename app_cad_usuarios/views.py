from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages

def home(request):
    return render(request, 'usuarios/home.html')

def listagem_usuarios(request):
    if request.method == "POST":
        Usuario.objects.create(
            nome=request.POST['nome'],  # Usando colchetes para forçar erro se faltar
            idade=request.POST['idade']
        )
        messages.success(request, 'Usuário cadastrado com sucesso!')  # 👈 Feedback
        return redirect('listagem_usuarios')  # 🚨 Sempre redirecione após POST

    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})