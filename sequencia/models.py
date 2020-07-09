from django.db import models
from clientes.models import Cliente
from mtr.models import Mtr


class Sequencia(models.Model):
    numero = models.AutoField(primary_key=True)
    mtr = models.ForeignKey(Mtr, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField('Rua',max_length=155)
    numero = models.IntegerField('Numero')
    bairro = models.CharField('Bairro', max_length=155)
    municipio = models.CharField('Municipio', max_length=155)
    estado = models.CharField('Estado', max_length=155)
