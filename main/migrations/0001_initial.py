# Generated by Django 3.1.6 on 2021-12-05 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacao', models.CharField(max_length=100)),
                ('uf', models.CharField(choices=[('MA', 'Maranhão'), ('PI', 'Piauí'), ('CE', 'Ceará'), ('RN', 'Rio Grande do Norte'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('AL', 'Alagoas'), ('SE', 'Sergipe'), ('BA', 'Bahia'), ('ES', 'Espírito Santo'), ('MG', 'Minas Gerais'), ('RJ', 'Rio de Janeiro'), ('SP', 'São Paulo'), ('PR', 'Paraná'), ('SC', 'Santa Catarina'), ('RS', 'Rio Grande do Sul'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('GO', 'Goiás'), ('TO', 'Tocantins'), ('DF', 'Distrito Federal'), ('RR', 'Roraima'), ('RO', 'Rondônia'), ('AC', 'Acre'), ('AM', 'Amazonas'), ('PA', 'Pará'), ('AP', 'Amapá')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Comunidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacao', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('eh_publica', models.BooleanField()),
                ('eh_visivel', models.BooleanField()),
                ('data_publicacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(blank=True, null=True, verbose_name='Texto da postagem')),
                ('eh_visivel', models.BooleanField(default=False)),
                ('data_publicacao', models.DateField(blank=True, null=True)),
                ('arquivo_de_midia', models.CharField(blank=True, max_length=200, null=True, verbose_name='Arquivo de mídia anexado')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('data_admissao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de admissão')),
                ('eh_ativo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioPostagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_avaliacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de avaliacao')),
                ('conceito', models.SmallIntegerField(choices=[(2, 'Interessante'), (4, 'Relevante'), (8, 'Destaque')])),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.postagem')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioComunidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.SmallIntegerField(choices=[(0, 'Solicitado'), (1, 'Aceito'), (-1, 'Recusado')])),
                ('data_situacao', models.DateTimeField(null=True)),
                ('comunidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comunidade')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='comunidades',
            field=models.ManyToManyField(through='main.UsuarioComunidade', to='main.Comunidade'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='postagens',
            field=models.ManyToManyField(through='main.UsuarioPostagem', to='main.Postagem'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='residencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cidade'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('data_publicacao', models.DateField()),
                ('comunidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comunidade')),
            ],
        ),
        migrations.AddField(
            model_name='postagem',
            name='signatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usuario', verbose_name='Signatário?'),
        ),
        migrations.AddField(
            model_name='postagem',
            name='topico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.topico', verbose_name='Tópico?'),
        ),
        migrations.AddField(
            model_name='comunidade',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.usuario'),
        ),
    ]