# Generated by Django 3.2.4 on 2022-05-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_sub_definition'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='color',
            field=models.CharField(default='white', max_length=40),
        ),
        migrations.AddField(
            model_name='post',
            name='sub_tittle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]