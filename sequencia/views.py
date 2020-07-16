from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Sequencia
from .serializers import SequenciaSerializers


class SequenciaViewset(ModelViewSet):
    queryset = Sequencia.objects.all()
    serializer_class = SequenciaSerializers
