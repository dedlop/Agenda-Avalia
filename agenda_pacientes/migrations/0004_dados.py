# Generated by Django 5.1.1 on 2024-09-21 00:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda_pacientes', '0003_rename_text_paciente_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contato', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda_pacientes.paciente')),
            ],
            options={
                'verbose_name_plural': 'dados',
            },
        ),
    ]
