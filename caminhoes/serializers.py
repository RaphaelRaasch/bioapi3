from .models import Caminhoes
from rest_framework.serializers import ModelSerializer


class CaminhaoSerializer(ModelSerializer):
    class Meta:
        model = Caminhoes
        fields = ('id', 'placa', 'nome')