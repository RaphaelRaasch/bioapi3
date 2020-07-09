from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from sequencia.models import Sequencia
from sequencia.serializers import SequenciaSerializer


class SequenciaViewSet(ModelViewSet):
    queryset = Sequencia.objects.all()
    serializer_class = SequenciaSerializer

#teste
