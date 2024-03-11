from django.db import models

# Create your models here.

class Departamento (models.Model):
    name=models.CharField('Nombre Departamento',max_length=30)
    shor_name=models.CharField('Nombre Corto' , max_length=20,blank=True,null=True,unique=True)
    anulate=models.BooleanField('Anulado', default=False)
    def __str__(self):
        return f'{self.id}- {self.name} - {self.shor_name}'

