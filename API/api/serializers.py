from rest_framework.serializers import ModelSerializer
from API.models import User, Analista, Supervisor, Pastor, Lider, participante, Igreja, Regiao, Celula, Relatorio, Endereco


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ()


class AnalistaSerializer(ModelSerializer):
    class Meta:
        model = Analista
        fields = (
            'id', 'user', 'regiao',
        )
        read_only_fields = ()


class SupervisorSerializer(ModelSerializer):
    class Meta:
        model = Supervisor
        fields = (
            'id', 'user', 'igreja',
        )
        read_only_fields = ()


class PastorSerializer(ModelSerializer):
    class Meta:
        model = Pastor
        fields = (
            'id', 'user', 'igreja',
        )
        read_only_fields = ()


class LiderSerializer(ModelSerializer):
    class Meta:
        model = Lider
        fields = (
            'id', 'user', 'igreja', 'celula',
        )
        read_only_fields = ()


class participanteSerializer(ModelSerializer):
    class Meta:
        model = participante
        fields = (
            'id', 'user', 'celula',
        )
        read_only_fields = ()


class IgrejaSerializer(ModelSerializer):
    class Meta:
        model = Igreja
        fields = (
            'id', 'pastor_titular', 'endereco', 'regiao', 'nome',
        )
        read_only_fields = ()


class RegiaoSerializer(ModelSerializer):
    class Meta:
        model = Regiao
        fields = (
            'id', 'nome',
        )
        read_only_fields = ()


class CelulaSerializer(ModelSerializer):
    class Meta:
        model = Celula
        fields = (
            'id', 'igreja', 'endereco', 'celula_pai', 'nome',
        )
        read_only_fields = ()


class RelatorioSerializer(ModelSerializer):
    class Meta:
        model = Relatorio
        fields = (
            'id', 'celula', 'tema', 'data', 'adultos', 'jovens', 'adolecentes', 'criancas', 'visitantes', 'homens',
            'mulheres', 'aceitacoes', 'recociliacoes', 'batismo', 'oferta', 'observacoes',
        )
        read_only_fields = ()


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'id', 'estado', 'cidade', 'bairro', 'endereco', 'numero', 'complemento',
        )
        read_only_fields = ()
