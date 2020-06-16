from django.db import models
from django.contrib.auth.models import User
from django.core.validators import  MinValueValidator

# Create your models here.


class Analista (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    regiao = models.ForeignKey('Regiao', null=True, on_delete=models.CASCADE)

    imagem = models.ImageField(upload_to='images/perfil/analista')

    def __str__(self):
        return self.user.get_short_name()


class Supervisor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    igreja = models.ForeignKey('Igreja', on_delete=models.CASCADE)

    imagem = models.ImageField(upload_to='images/perfil/supervisor')

    def __str__(self):
        return self.user.get_short_name()


class Pastor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    igreja = models.ForeignKey('Igreja', on_delete=models.CASCADE)

    imagem = models.ImageField(upload_to='images/perfil/pastor')

    def __str__(self):
        return self.user.get_short_name()


class Lider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    igreja = models.ForeignKey('Igreja', on_delete=models.CASCADE)
    celula = models.ForeignKey('Celula', on_delete=models.CASCADE)

    imagem = models.ImageField(upload_to='images/perfil/lider')

    def __str__(self):
        return self.user.get_short_name()


class participante(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    celula = models.ForeignKey('Celula', on_delete=models.CASCADE)

    imagem = models.ImageField(upload_to='images/perfil/participante')

    def __str__(self):
        return self.user.get_short_name()


class Igreja(models.Model):
    pastor_titular = models.ForeignKey(Pastor, on_delete=models.CASCADE, related_name='igreja_titular')
    endereco = models.OneToOneField('Endereco', on_delete=models.CASCADE)
    regiao = models.ForeignKey('Regiao', on_delete=models.CASCADE)

    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome+', '+self.regiao.nome


class Regiao(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Celula(models.Model):

    class SEMANA(models.TextChoices):
        Dom = 'Dom', ('Domingo'),
        Seg = 'Seg', ('Segunda-feira')
        Ter = 'Ter', ('Terça-feira')
        Qua = 'Qua', ('Quarta-feira')
        Qui = 'Qui', ('Quinta-feira')
        Sex = 'Sex', ('Sexta-feira')
        Sab = 'Sab', ('Sabado')

    igreja = models.ForeignKey(Igreja, on_delete=models.CASCADE)
    endereco = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    celula_pai = models.ForeignKey('Celula', on_delete=models.DO_NOTHING)

    dia = models.CharField(max_length=3, choices=SEMANA, default=SEMANA.Sab)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    def dia(self):
        return self.SEMANA.find(self.dia)


class Relatorio(models.Model):
    celula = models.ForeignKey(Celula, on_delete=models.CASCADE)

    tema = models.CharField(max_length=50)
    data = models.DateField(auto_now=True)
    adultos = models.IntegerField(validators=[MinValueValidator(0)])
    jovens = models.IntegerField(validators=[MinValueValidator(0)])
    adolecentes = models.IntegerField(validators=[MinValueValidator(0)])
    criancas = models.IntegerField(validators=[MinValueValidator(0)])
    visitantes = models.IntegerField(validators=[MinValueValidator(0)])
    homens = models.IntegerField(validators=[MinValueValidator(0)])
    mulheres = models.IntegerField(validators=[MinValueValidator(0)])

    aceitacoes = models.IntegerField(validators=[MinValueValidator(0)])
    recociliacoes = models.IntegerField(validators=[MinValueValidator(0)])
    batismo = models.IntegerField(validators=[MinValueValidator(0)])

    oferta = models.FloatField(validators=[MinValueValidator(0)])

    observacoes = models.TextField()

    def __str__(self):
        return self.tema+' / '+str(self.data)


class Endereco(models.Model):
    estado = models.CharField(max_length=30)
    cidade = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    endereco = models.CharField(max_length=60)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=50)

    def __str__(self):
        return self.bairro+" - "+self.endereco


class Foto():
    relatorio = models.ForeignKey(Relatorio, on_delete=models.CASCADE)

    imagem = models.ImageField(upload_to='images/galeria/% Y/% m/% d')
    data = models.DateField(auto_created=True)
