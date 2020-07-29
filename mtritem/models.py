from django.db import models
from mtr.models import Mtr
from motoristas.models import Motoristas
from sequencia.models import Sequencia


class MtrItem(models.Model):
    mtr = models.ForeignKey(Mtr, on_delete=models.CASCADE)
    sequencia = models.ManyToManyField(Sequencia)
