from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == "POST":
        novo_usuario = Usuario(
            nome=request.POST.get('nome'),
            idade=request.POST.get('idade')
        )
        novo_usuario.save()

    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

def listagem_usuarios(request):
    usuarios = Usuario.objects.all()
    print(f"Total de usuários encontrados: {usuarios.count()}")
    for usuario in usuarios:
        print(f"ID: {usuario.id_usuario}, Nome: {usuario.nome}, Idade: {usuario.idade}")
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})