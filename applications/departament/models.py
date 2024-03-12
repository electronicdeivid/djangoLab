from django.db import models

# Create your models here.
class Departament (models.Model):
  name=models.CharField('Departament Name',max_length=30)
  shor_name=models.CharField('Short Name' , max_length=20,blank=True,null=True,unique=True)
  anulate=models.BooleanField('Anulated', default=False)
  
  class Meta:
    verbose_name='Departamento'
    verbose_name_plural='Departamentos' 
    ordering=('name',) 
    unique_together=('name',)

  def __str__(self):
    return f'{self.shor_name} - {self.name}'
  
  
