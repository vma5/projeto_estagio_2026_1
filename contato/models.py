from django.db import models

class Mensagem(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=150, blank=True, verbose_name="Assunto")
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    class Meta:
        ordering = ['-data_envio']
        verbose_name = "Mensagem"

    def __str__(self):
        return f"{self.nome} - {self.email}"