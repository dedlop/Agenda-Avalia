# Generated by Django 5.1.1 on 2024-09-20 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda_pacientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='nome',
            new_name='text',
        ),
    ]