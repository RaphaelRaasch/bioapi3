from django.db import models


class Caminhoes(models.Model):
    placa = models.CharField('Placa', max_length=7)
    nome = models.CharField('Nome', max_length=30)
