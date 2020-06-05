from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from motoristas.views import MotoristaViewSet
from mtr.views import MtrViewSet
from caminhoes.views import CaminhaoViewSet
from clientes.views import ClienteViewSet
from .views import UserViewSet
from .customtoken import CustomAuthToken

router = routers.DefaultRouter()
router.register(r'motoristas', MotoristaViewSet)
router.register(r'mtr', MtrViewSet)
router.register(r'caminhoes', CaminhaoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', admin.site.urls),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

