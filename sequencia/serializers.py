<<<<<<< Updated upstream
from .models import Sequencia
from rest_framework.serializers import ModelSerializer
from clientes.serializers import ClienteSerializer

class SequenciaSerializer(ModelSerializer):
    
    cliente = ClienteSerializer(many=False)

    class Meta:
        model = Sequencia
        fields = ('position', 'rua','numero','bairro','municipio','complemento', 'cliente')
=======
from rest_framework.serializers import ModelSerializer
from .models import Sequencia
from clientes.serializers import ClienteSerializer 


class SequenciaSerializers(ModelSerializer):
    cliente = ClienteSerializer(many=False)

    
    class Meta:
        model = Sequencia
        fields = ('numero', 'mtr', 'cliente', 'rua', 'numero', 'bairro', 'municipio', 'estado')
>>>>>>> Stashed changes
