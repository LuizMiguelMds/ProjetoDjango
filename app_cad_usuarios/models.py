from django.db import models

# models.py
class Usuario(models.Model):
    # REMOVA a linha id_usuario se existir
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"  # 👈 Agora mostra nomes no QuerySet