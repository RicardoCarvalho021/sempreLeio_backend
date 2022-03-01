# Generated by Django 3.1.6 on 2022-02-21 13:22

from django.db import migrations
from django.db import models, migrations
from django.conf import settings
from django.contrib.auth.models import User
from main.models import Postagem, Usuario, Cidade, Comunidade, Topico, UsuarioComunidade
from datetime import datetime
import os

#-------------------------------------------------------------
# Script para popular inicialmente o DB com dados para testes.
# Vicente Limeira
# 27-2-2022
#-------------------------------------------------------------

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        userAdmin = User(username='admin',
                    email='teste@teste.com',
                    is_staff=True,
                    is_superuser=True,
                    )
        userAdmin.set_password('teste@123')
        userAdmin.save()

        cidade1 = Cidade(denominacao='Natal', uf='RN',)
        cidade1.save()
        user1 = User(
                    username='vicente',
                    first_name='Vicente',
                    last_name='Limeira',
                    email='vicente@teste.com',
                    is_staff=True,
                    is_active=True,
                    is_superuser=False,
                    date_joined=datetime.now().date(),
        )
        user1.set_password('teste@123')
        user1.save()
        usuario1 = Usuario(
                    nome='Vicente Limeira',
                    email='vicente@teste.com',
                    cpf = '67299924434',
                    data_admissao  = datetime.now().date(),
                    eh_ativo = True,
                    residencia=cidade1,
                    user=user1,
                    )
        usuario1.save()

        cidade2 = Cidade(denominacao='Recife', uf='PE',)
        cidade2.save()
        user2 = User(
                    username='andre',
                    first_name='André',
                    last_name='Nascimento',
                    email='andre@teste.com',
                    is_staff=True,
                    is_active=True,
                    is_superuser=False,
                    date_joined=datetime.now().date(),
        )
        user2.set_password('teste@123')
        user2.save()
        usuario2 = Usuario(
                    nome='André Nascimento',
                    email='andre@teste.com',
                    cpf = '67299924435',
                    data_admissao  = datetime.now().date(),
                    eh_ativo = True,
                    residencia=cidade2,
                    user=user2,
                    )
        usuario2.save()

        cidade3 = Cidade(denominacao='Salvador', uf='BA',)
        cidade3.save()
        user3 = User(
                    username='ricardo',
                    first_name='Ricardo',
                    last_name='Rafael',
                    email='ricardo@teste.com',
                    is_staff=True,
                    is_active=True,
                    is_superuser=False,
                    date_joined=datetime.now().date(),
        )
        user3.set_password('teste@123')
        user3.save()
        usuario3 = Usuario(
                    nome='Ricardo Rafael',
                    email='ricardo@teste.com',
                    cpf = '67299924436',
                    data_admissao  = datetime.now().date(),
                    eh_ativo = True,
                    residencia=cidade3,
                    user=user3,
                    )
        usuario3.save()

        comunidade1 = Comunidade(
                denominacao = 'Vida e obra de Machado de Assis',
                descricao = 'O propósito desta homenagem a Machado de Assis, mais que lembrar o centenário de sua morte, é fazer com que a sua obra completa chegue a qualquer usuário internet, em edições confiáveis e gratuitas. Resultado de uma parceria entre o Portal Domínio Público - a biblioteca digital do MEC - e o Núcleo de Pesquisa em Informática, Literatura e Lingüística (NUPILL), da Universidade Federal de Santa Catarina, o projeto teve como propósito organizar, sistematizar, complementar e revisar as edições digitais até então existentes na rede, gerando o que se pode chamar de Coleção Digital Machado de Assis.',
                eh_publica = True,
                eh_visivel = True,
                data_publicacao = datetime.now().date(),
                proprietario = usuario1,
        )
        comunidade1.save()

        comunidade2 = Comunidade(
                denominacao = 'Clarice Lispector',
                descricao = '... Sim, minha força está na solidão. Não tenho medo nem de chuvas tempestivas nem das grandes ventanias soltas, pois eu também sou o escuro da noite.',
                eh_publica = True,
                eh_visivel = True,
                data_publicacao = datetime.now().date(),
                proprietario = usuario2,
        )
        comunidade2.save()        

        comunidade3 = Comunidade(
                denominacao = 'Geração 1945',
                descricao = 'A geração de 1945 corresponde a um dos mais importantes e produtivos momentos da Literatura brasileira. Também conhecida como terceira geração modernista, surgiu em um contexto histórico interessante, o que propiciou uma experiência literária voltada para a questão estética.',
                eh_publica = True,
                eh_visivel = True,
                data_publicacao = datetime.now().date(),
                proprietario = usuario3,
        )
        comunidade3.save()        

        topico1 = Topico(
                titulo = 'Quem foi Machado de Assis?',
                data_publicacao = datetime.now().date(),
                comunidade = comunidade1
        )
        topico1.save()

        topico2 = Topico(
                titulo = 'Quais são as características de Machado de Assis?',
                data_publicacao = datetime.now().date(),
                comunidade = comunidade1
        )
        topico2.save()

        membro1 = UsuarioComunidade(
                situacao = 1,
                data_situacao = datetime.now().date(),
                usuario = usuario2,
                comunidade = comunidade1,
        )
        membro1.save()

        membro2 = UsuarioComunidade(
                situacao = 0,
                data_situacao = datetime.now().date(),
                usuario = usuario3,
                comunidade = comunidade1,
        )
        membro2.save()

        postagem1 = Postagem(
                texto = 'Machado de Assis nasceu em 21 de junho de 1839, no Morro do Livramento, localizado no Rio de Janeiro. Machado de Assis perdeu a mãe e a irmã ainda muito jovem. Começou seus trabalhos na área jornalística sendo aprendiz de tipógrafo na Tipografia Nacional, trabalhando junto com o também escritor brasileiro Manuel Antônio de Almeida — autor de “Memórias de um Sargento de Milícias”. Machado nasceu em família carente, mas letrada e, por isso, mesmo sem frequentar a escola, era capaz de ler e escrever. Descendente de negros, gago e epilético, conseguiu grande ascensão na vida e carreira, tendo sido oficial da Ordem da Rosa, além de ter ocupado outros cargos públicos. No entanto, foi no jornalismo que Machado de Assis destacou-se por escrever crônicas diárias sobre, inicialmente, as sessões parlamentares e, posteriormente, sobre o cotidiano da cidade do Rio de Janeiro, que passava por mudanças inspiradas no urbanismo parisiense. Escrevendo para os jornais, passou anos compondo pequenos relatos do cotidiano, tendo a autoria de mais de 600 crônicas, que acabaram por inspirá-lo na sua jornada pelo Realismo, sendo aqui no Brasil seu precursor. Em 1897, fundou a Academia Brasileira de Letras, onde foi presidente por 10 anos. Em 1908, morreu e foi enterrado junto com sua esposa, Carolina Augusta Xavier de Novais, no cemitério de São João Batista no Rio de Janeiro.',
                eh_visivel = True,
                data_publicacao = datetime.now().date(),
                topico = topico1,
                signatario = usuario2,
        )
        postagem1.save()

        postagem2 = Postagem(
                texto = 'As características principais das obras de Machado de Assis são: crítica à burguesia e à sociedade de maneira geral, ironia, metalinguagem e o diálogo direto com o leitor. Sua obra também é bastante conhecida pelo chamado realismo psicológico, que se caracteriza pelos aspectos psicológicos dos personagens, os quais, até então, eram explorados apenas a nível físico e costumeiro. Por ser um escritor que também era jornalista e cronista, sua visão da sociedade, a qual rotineiramente observava, influenciava muito o que abordava em suas obras: a sociedade burguesa carioca do século XIX.',
                eh_visivel = True,
                data_publicacao = datetime.now().date(),
                topico = topico2,
                signatario = usuario1,
        )
        postagem2.save()

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data,),
    ]
    
