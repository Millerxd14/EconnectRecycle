# Generated by Django 3.2.4 on 2022-10-14 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221013_2222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='update_counter',
            new_name='contador_actualizar',
        ),
    ]
