from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from .models import Sequencia
from .serializers import SequenciaSerializers


class SequenciaViewset(ViewSet):
    queryset = Sequencia.objects.all()
    serializer_class = SequenciaSerializers
