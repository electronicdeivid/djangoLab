from django.db import models
from applications.departament.models import Departament
# Create your models here.

class Employee(models.Model):
    job_choices=(('0','Counter'),
                 ('1','Administrator'),
                 ('2','Economist'),
                 ('3','Developer'))
    ''' Modelo para tabla de empleado'''
    first_name = models.CharField('Names', max_length=60)
    last_name = models.CharField('Lastnames', max_length=60)
    job=models.CharField('Job',max_length=1,choices=job_choices)
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE)

    def __str__(self):
      for n,role in self.job_choices:
        if n==self.job:
          return f'{self.id}- {self.first_name} - {role}'
    