from .models import MtrV2
from rest_framework.viewsets import ModelViewSet
from .serializers import Mtrv2Serializer


class MtrV2ViewSet(ModelViewSet):
    queryset = MtrV2.objects.all()
    serializer_class = Mtrv2Serializer
