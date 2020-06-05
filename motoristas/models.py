from biotrack.settings import AUTH_USER_MODEL
from django.db import models


class Motoristas(models.Model):
    id_multidev = models.IntegerField('Id Multidev')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField('Nome', max_length=115)
    cpf = models.CharField('CPF', max_length=11)
    mopp = models.CharField('MOPP', max_length=20, blank=True, null=True)
    mopp_validade = models.DateField('Validade MOPP', blank=True, null=True)
    cnh = models.CharField('CNH', max_length=20)
    cnh_categoria = models.CharField('Categoria Cnh', max_length=2)
    cnh_validade = models.DateField('Validade CNH')
    
    def __str__(self):
       return self.nome
