# Generated by Django 3.2.4 on 2022-05-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='dni',
            field=models.CharField(default='unamed', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_collector',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_productor',
            field=models.BooleanField(default=False),
        ),
    ]
