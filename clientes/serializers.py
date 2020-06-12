from .models import Cliente
from rest_framework.serializers import ModelSerializer


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'id_multidev', 'razao_social', 'destao', 'fantasia','logradouro','bairro','municipio','estado', 'latitude', 'longitude')
