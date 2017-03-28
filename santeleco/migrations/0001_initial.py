# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('actividad', models.CharField(max_length=128)),
                ('deportiva', models.BooleanField()),
                ('dia', models.DateField()),
                ('lugar', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('curso', models.IntegerField()),
                ('actividad', models.ForeignKey(to='santeleco.Actividad')),
                ('grado', models.ForeignKey(to='santeleco.Grado')),
            ],
        ),
    ]
