# Generated by Django 3.0.7 on 2020-06-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20200613_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='analista',
            name='imagem',
            field=models.ImageField(default=0, upload_to='images/perfil/analista'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lider',
            name='imagem',
            field=models.ImageField(default=0, upload_to='images/perfil/lider'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participante',
            name='imagem',
            field=models.ImageField(default=0, upload_to='images/perfil/participante'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pastor',
            name='imagem',
            field=models.ImageField(default=0, upload_to='images/perfil/pastor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisor',
            name='imagem',
            field=models.ImageField(default=0, upload_to='images/perfil/supervisor'),
            preserve_default=False,
        ),
    ]
