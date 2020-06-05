from .models import Caminhoes
from rest_framework.viewsets import ModelViewSet
from .serializers import CaminhaoSerializer


class CaminhaoViewSet(ModelViewSet):
    queryset = Caminhoes.objects.all()
    serializer_class = CaminhaoSerializer

