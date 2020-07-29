from django.db import models
from mtr.models import Mtr
from motoristas.models import Motoristas
from sequencia.models import Sequencia


# Create your models here.
class MtrV2(models.Model):
    mtr = models.ForeignKey(Mtr, on_delete=models.CASCADE)
    motorista = models.ForeignKey(Motoristas, on_delete=models.CASCADE)
    sequencia = models.ManyToManyField(Sequencia)
