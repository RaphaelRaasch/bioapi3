from rest_framework.serializers import ModelSerializer
from .models import MtrV2
from sequencia.serializers import SequenciaSerializers

class Mtrv2Serializer(ModelSerializer):
    
    sequencia = ()
    class Meta:
        model = MtrV2
        fields = ('mtr','motorista','sequencia')


