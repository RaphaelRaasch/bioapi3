
from rest_framework.serializers import ModelSerializer
from .models import Sequencia 


class SequenciaSerializers(ModelSerializer):
    
    class Meta:
        model = Sequencia
        fields = ('numero', 'mtr', 'cliente', 'rua', 'numero', 'bairro', 'municipio', 'estado')
