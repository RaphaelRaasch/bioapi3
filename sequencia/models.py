from django.db import models
from clientes.models import Cliente

class Sequencia(models.Model):
    position = models.IntegerField('Position')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField('Rua', max_length=155)
    numero = models.IntegerField('Numero')
    bairro = models.CharField('Bairro', max_length=155)
    municipio = models.CharField('Municipio', max_length=155)
    