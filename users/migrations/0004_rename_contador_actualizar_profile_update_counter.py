# Generated by Django 3.2.4 on 2022-10-14 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_update_counter_profile_contador_actualizar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='contador_actualizar',
            new_name='update_counter',
        ),
    ]