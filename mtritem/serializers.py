from rest_framework.serializers import ModelSerializer
from .models import MtrItem
from sequencia.serializers import SequenciaSerializers

class MtrItemSerializer(ModelSerializer):
    
    sequencia = ()
    class Meta:
        model = MtrItem
        fields = ('mtr','sequencia')