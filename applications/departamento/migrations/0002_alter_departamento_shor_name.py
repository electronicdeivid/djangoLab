# Generated by Django 4.2.11 on 2024-03-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
