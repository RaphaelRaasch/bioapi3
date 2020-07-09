from biotrack.settings import AUTH_USER_MODEL
from django.db import models
from clientes.models import Cliente
from caminhoes.models import Caminhoes
from sequencia.models import Sequencia


class Mtr(models.Model):
    numero = models.IntegerField('Numero')
    motorista = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    alias = models.CharField('alias', max_length=155) 
    saida = models.DateTimeField('Data e hora da saida', blank=True, null=True)
    chegada = models.DateTimeField('Data e hora da chegada', blank=True, null=True)
    caminhao = models.ForeignKey(Caminhoes, on_delete=models.CASCADE)
    sequencia = models.ManyToManyField(Sequencia)

    def __str__(self):
       return self.alias

