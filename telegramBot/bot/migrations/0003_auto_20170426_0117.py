# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_documento_imagem_texto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='documento',
            field=models.FileField(upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
