# Generated by Django 3.0.7 on 2020-06-17 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_auto_20200617_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_created=True)),
                ('imagem', models.ImageField(upload_to='images/galeria/% Y/% m/% d')),
                ('relatorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Relatorio')),
            ],
        ),
    ]