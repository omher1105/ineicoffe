# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-24 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.PositiveIntegerField(choices=[(1, 'Agradecimiento'), (2, 'Sugerencia'), (3, 'Reclamo')])),
                ('primer_nombre', models.CharField(max_length=100)),
                ('segundo_nombre', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('asunto', models.CharField(max_length=100)),
                ('contenido', models.TextField(blank=True, default=None, null=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
