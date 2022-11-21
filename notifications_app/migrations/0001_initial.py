# Generated by Django 3.2.4 on 2022-10-14 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(max_length=255)),
                ('broadcast_on', models.DateTimeField()),
                ('tipo', models.CharField(default='0', max_length=25)),
                ('estado', models.CharField(default='0', max_length=25)),
                ('direccion', models.CharField(default='caneca', max_length=25)),
                ('usuario_enviador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remitente', to=settings.AUTH_USER_MODEL)),
                ('usuario_propietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='propietario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-broadcast_on'],
            },
        ),
    ]