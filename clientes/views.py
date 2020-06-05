from .models import Cliente
from rest_framework.viewsets import ModelViewSet
from .serializers import ClienteSerializer


class ClienteViewSet(ModelViewSet):    
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

