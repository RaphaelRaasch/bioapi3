from django.shortcuts import render
<<<<<<< Updated upstream
from rest_framework.viewsets import ModelViewSet
from sequencia.models import Sequencia
from sequencia.serializers import SequenciaSerializer


class SequenciaViewSet(ModelViewSet):
    queryset = Sequencia.objects.all()
    serializer_class = SequenciaSerializer

#teste
=======
from rest_framework.viewsets import ViewSet
from .models import Sequencia
from .serializers import SequenciaSerializers


class SequenciaViewset(ViewSet):
    queryset = Sequencia.objects.all()
    serializer_class = SequenciaSerializers
>>>>>>> Stashed changes
