from django.db import models


class Cliente(models.Model):
    id_multidev = models.IntegerField('Id Multidev')
    razao_social = models.CharField('Razão Social', max_length=115)
    fantasia = models.CharField('Nome Fantasia', max_length=115)
    logradouro = models.CharField('Logradouro', max_length=115, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=115, blank=True, null=True)
    municipio = models.CharField('Municipio', max_length=115, blank=True, null=True) 
    estado = models.CharField('Estado', max_length=115, blank=True, null=True)
    latitude = models.CharField('Latitude', max_length=100)
    longitude = models.CharField('Longitude', max_length=100)

    def __str__(self):
        return self.fantasia





"""
id_multidev int
razao_social varchar(115)
fantasia varchar(115)
latitude
longitude
"""
