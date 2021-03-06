from django.conf.urls import url, include
from rest_framework import routers

from API.api.viewsets import UserViewSet, AnalistaViewSet, SupervisorViewSet, PastorViewSet, LiderViewSet, participanteViewSet, IgrejaViewSet, \
    RegiaoViewSet, CelulaViewSet, RelatorioViewSet, EnderecoViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'analistas', AnalistaViewSet)
router.register(r'supervisors', SupervisorViewSet)
router.register(r'pastors', PastorViewSet)
router.register(r'liders', LiderViewSet)
router.register(r'participantes', participanteViewSet)
router.register(r'igrejas', IgrejaViewSet)
router.register(r'regiaos', RegiaoViewSet)
router.register(r'celulas', CelulaViewSet)
router.register(r'relatorios', RelatorioViewSet)
router.register(r'enderecos', EnderecoViewSet)

from rest_framework.authtoken import views

urlpatterns = [
    url(r'^', include(router.urls)),
]
