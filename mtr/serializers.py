from .models import Mtr
from rest_framework.serializers import ModelSerializer
from clientes.serializers import ClienteSerializer

class MtrSerializer(ModelSerializer):
    
    cliente = ClienteSerializer(many=True)

    class Meta:
        model = Mtr
        fields = ('id', 'numero', 'motorista', 'alias', 'saida', 'chegada', 'cliente', 'caminhao')


'''
    numero = models.IntegerField('Numero')
    motorista = models.ForeignKey(User, on_delete=models.CASCADE)
    alias = models.CharField('alias', max_length=155)
    saida = models.DateTimeField('Data e hora da saida', blank=True, null=True)
    chegada = models.DateTimeField('Data e hora da chegada', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    caminhao = models.ForeignKey(Caminhoes, on_delete=models.CASCADE)

'''
