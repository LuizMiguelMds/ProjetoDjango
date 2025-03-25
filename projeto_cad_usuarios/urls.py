from django.urls import path
from app_cad_usuarios import views  # 👈 Corrigido para importar do app correto

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),  # 🔥 Única view para listar/cadastrar
]