# Generated by Django 4.2.11 on 2024-03-13 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=30, verbose_name='Skill')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.AddField(
            model_name='employee',
            name='skill',
            field=models.ManyToManyField(to='employees.skill'),
        ),
    ]