# Generated by Django 4.2.11 on 2024-03-11 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='Mes')),
                ('subtitulo', models.CharField(max_length=50, verbose_name='Meta/s')),
            ],
        ),
    ]
