from .models import Motoristas
from rest_framework.viewsets import ModelViewSet
from .serializers import MotoristaSerializer


class MotoristaViewSet(ModelViewSet):
    queryset = Motoristas.objects.all()
    serializer_class = MotoristaSerializer

