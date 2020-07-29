from biotrack.settings import AUTH_USER_MODEL
from django.db import models
from motoristas.models import Motoristas
from clientes.models import Cliente
from caminhoes.models import Caminhoes


class Mtr(models.Model):
    numero = models.IntegerField('Numero')
    motorista = models.ForeignKey(Motoristas, on_delete=models.CASCADE)
    alias = models.CharField('alias', max_length=155) 
    saida = models.DateTimeField('Data e hora da saida', blank=True, null=True)
    chegada = models.DateTimeField('Data e hora da chegada', blank=True, null=True)
    caminhao = models.ForeignKey(Caminhoes, on_delete=models.CASCADE)
    def __str__(self):
       return self.alias

