from django.db import models

# Create your models here.

class Departament (models.Model):
    name=models.CharField('Departament Name',max_length=30)
    shor_name=models.CharField('Short Name' , max_length=20,blank=True,null=True,unique=True)
    anulate=models.BooleanField('Anulated', default=False)
    def __str__(self):
        return f'{self.id}- {self.name} - {self.shor_name}'

