from .models import MtrItem
from rest_framework.viewsets import ModelViewSet
from .serializers import MtrItemSerializer


class MtrItemViewSet(ModelViewSet):
    queryset = MtrItem.objects.all()
    serializer_class = MtrItemSerializer
