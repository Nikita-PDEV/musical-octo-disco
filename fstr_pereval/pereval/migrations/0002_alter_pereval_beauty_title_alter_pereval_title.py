# Generated by Django 5.1.4 on 2024-12-06 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pereval',
            name='beauty_title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название препятствия'),
        ),
        migrations.AlterField(
            model_name='pereval',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Название вершины'),
        ),
    ]
