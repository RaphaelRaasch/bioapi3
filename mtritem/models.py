from django.db import models
from mtr.models import Mtr
from motoristas.models import Motoristas
from sequencia.models import Sequencia


class MtrItem(models.Model):
    mtr = models.ForeignKey(Mtr, on_delete=models.CASCADE)
    sequencia = models.ManyToManyField(Sequencia)
    latitude = models.CharField('Latitude', max_length=150)
    longitude = models.CharField('Longitude', max_length=150)
    def __str__(self):
        return f'{self.mtr}'
    
