from rest_framework.serializers import ModelSerializer
from .models import MtrItem
from sequencia.serializers import SequenciaSerializers
from mtr.serializers import MtrSerializer
class MtrItemSerializer(ModelSerializer):
    
    sequencia = SequenciaSerializers(many=True)
    mtr = MtrSerializer(many=False, read_only=True), 
    class Meta:
        model = MtrItem
        fields = ('id','mtr','sequencia','latitude','longitude')