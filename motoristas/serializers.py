from .models import Motoristas
from rest_framework.serializers import ModelSerializer


class MotoristaSerializer(ModelSerializer):
    class Meta:
        model = Motoristas
        fields = ('id', 'id_multidev', 'user', 'nome', 'cpf', 'mopp', 'mopp_validade', 'cnh', 'cnh_categoria', 'cnh_validade')




"""
    id_multidev = models.IntegerField('Id Multidev')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=115)
    cpf = models.CharField('CPF', max_length=11)
    mopp = models.CharField('MOPP', max_length=20, blank=True, null=True)
    mopp_validade = models.DateField('Validade MOPP', blank=True, null=True)
    cnh = models.CharField('CNH', max_length=20)
    cnh_categoria = models.CharField('Categoria Cnh', max_length=2)
    cnh_validade = models.DateField('Validade CNH')
    latitude = models.CharField('Latitude', max_length=100)
    longitude = models.CharField('Longitude', max_length=100)
"""
