# Generated by Django 3.1.6 on 2022-02-20 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_topico_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topico',
            name='teste',
        ),
    ]