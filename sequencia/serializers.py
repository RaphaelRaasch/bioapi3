from .models import Sequencia
from rest_framework.serializers import ModelSerializer
from clientes.serializers import ClienteSerializer

class SequenciaSerializer(ModelSerializer):
    
    cliente = ClienteSerializer(many=False)

    class Meta:
        model = Sequencia
        fields = ('position', 'rua','numero','bairro','municipio','complemento', 'cliente')