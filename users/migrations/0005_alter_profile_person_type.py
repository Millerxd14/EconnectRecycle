# Generated by Django 3.2.4 on 2022-05-23 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='person_type',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
