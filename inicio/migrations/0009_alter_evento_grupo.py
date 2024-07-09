# Generated by Django 5.0.6 on 2024-07-08 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0008_evento_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inicio.grupo', verbose_name='Grupo'),
        ),
    ]
