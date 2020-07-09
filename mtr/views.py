from .models import Mtr
from rest_framework.viewsets import ModelViewSet
from .serializers import MtrSerializer


class MtrViewSet(ModelViewSet):
    queryset = Mtr.objects.all()
    serializer_class = MtrSerializer

