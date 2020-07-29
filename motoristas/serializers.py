from .models import Motoristas
from rest_framework.serializers import ModelSerializer


class MotoristaSerializer(ModelSerializer):
    class Meta:
        model = Motoristas
        fields = ('id', 'id_multidev', 'user', 'nome', 'cpf', 'mopp', 'mopp_validade', 'cnh', 'cnh_categoria', 'cnh_validade')

