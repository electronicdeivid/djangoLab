# Generated by Django 4.2.11 on 2024-03-12 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departament', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departament',
            options={'ordering': ('name',), 'verbose_name': 'Departamento', 'verbose_name_plural': 'Departamentos'},
        ),
        migrations.AlterUniqueTogether(
            name='departament',
            unique_together={('name',)},
        ),
    ]
