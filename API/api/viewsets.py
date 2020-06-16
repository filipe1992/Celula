from rest_framework import viewsets
from API.models import User, Analista, Supervisor, Pastor, Lider, participante, Igreja, Regiao, Celula, Relatorio, Endereco
from API.api.serializers import UserSerializer, AnalistaSerializer, SupervisorSerializer, PastorSerializer, LiderSerializer, participanteSerializer, \
    IgrejaSerializer, RegiaoSerializer, CelulaSerializer, RelatorioSerializer, EnderecoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = (
        'id'
    )
    filter_fields = (
        'id',
    )
    ordering_fields = (
        'id'
    )


class AnalistaViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Analista.objects.all()
    serializer_class = AnalistaSerializer
    search_fields = (

    )
    filter_fields = (
        'user', 'regiao',
    )
    ordering_fields = (
        'id', 'user', 'regiao',
    )


class SupervisorViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer
    search_fields = (
        'igreja',
    )
    filter_fields = (
        'user', 'igreja',
    )
    ordering_fields = (
        'id', 'user', 'igreja',
    )


class PastorViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Pastor.objects.all()
    serializer_class = PastorSerializer
    search_fields = (
        'igreja',
    )
    filter_fields = (
        'user', 'igreja',
    )
    ordering_fields = (
        'id', 'user', 'igreja',
    )


class LiderViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Lider.objects.all()
    serializer_class = LiderSerializer
    search_fields = (
        'igreja', 'celula',
    )
    filter_fields = (
        'user', 'igreja', 'celula',
    )
    ordering_fields = (
        'id', 'user', 'igreja', 'celula',
    )


class participanteViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = participante.objects.all()
    serializer_class = participanteSerializer
    search_fields = (
        'celula',
    )
    filter_fields = (
        'user', 'celula',
    )
    ordering_fields = (
        'id', 'user', 'celula',
    )


class IgrejaViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Igreja.objects.all()
    serializer_class = IgrejaSerializer
    search_fields = (
        'nome',
    )
    filter_fields = (
        'pastor_titular', 'endereco', 'regiao', 'nome',
    )
    ordering_fields = (
        'id', 'pastor_titular', 'endereco', 'regiao', 'nome',
    )


class RegiaoViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Regiao.objects.all()
    serializer_class = RegiaoSerializer
    search_fields = (
        'nome',
    )
    filter_fields = (
        'id', 'nome',
    )
    ordering_fields = (
        'id', 'nome',
    )


class CelulaViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Celula.objects.all()
    serializer_class = CelulaSerializer
    search_fields = (
        'nome',
    )
    filter_fields = (
        'igreja', 'endereco', 'celula_pai', 'nome',
    )
    ordering_fields = (
        'id', 'igreja', 'endereco', 'celula_pai', 'nome',
    )


class RelatorioViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    search_fields = (
        'tema', 'data', 'celula',
    )
    filter_fields = (
        'tema', 'data', 'celula',
    )
    ordering_fields = (
        'id', 'celula', 'tema', 'data', 'adultos', 'jovens', 'adolecentes', 'criancas', 'visitantes', 'homens',
        'mulheres', 'aceitacoes', 'recociliacoes', 'batismo', 'oferta', 'observacoes',
    )


class EnderecoViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    search_fields = (
        'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento',
    )
    filter_fields = (
        'id', 'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento',
    )
    ordering_fields = (
        'id', 'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento',
    )
