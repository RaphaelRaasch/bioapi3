from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from biotrack.customtoken import CustomAuthToken
from caminhoes.views import CaminhaoViewSet
from clientes.views import ClienteViewSet
from motoristas.views import MotoristaViewSet
from mtr.views import MtrViewSet
from mtrv2.views import MtrV2ViewSet
from sequencia.views import SequenciaViewset

router = routers.DefaultRouter()
router.register(r'mtr', MtrViewSet)
router.register(r'mtrv2', MtrV2ViewSet)
router.register(r'cliente', ClienteViewSet)


router.register(r'sequencia', SequenciaViewset)
router.register(r'motoristas', MotoristaViewSet)
router.register(r'caminhao', CaminhaoViewSet)



urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth-token/', CustomAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
