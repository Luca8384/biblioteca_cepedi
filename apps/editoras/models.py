from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome da Editora')
    telefone = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'Editora'
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['nome']
