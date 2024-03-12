from django.db import models

#---------- Create your models here.------------


#class Tasks(models.Model):
#    task=models.CharField('tarea',max_length=30)

class Prueba(models.Model):
  #Shields of my model
  mes=models.CharField('Mes',max_length=30)
  meta = models.CharField('Meta/s',max_length=50)
 # responsabilidades=models.ManyToOneRel

  class Meta:
      unique_together=('mes',)      
    #Functions of my model
  def __str__(self):
    return f'{self.mes}: {self.meta}'

#lass Tasks(models.Model):
#    task=models.CharField('tarea',max_length=30)
#    tasks=models.ManyToManyField(Prueba)


