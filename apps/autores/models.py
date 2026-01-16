from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome do Autor')









    def __str__(self):
        return self.nome


    class Meta:
        db_table = 'Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
