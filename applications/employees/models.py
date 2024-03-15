from django.db import models
from applications.departament.models import Departament
# Create your models here.

class Skill(models.Model):
  skill=models.CharField('Skills',max_length=30)

  class Meta:
    verbose_name='skill'
    verbose_name_plural='skills'

  def __str__(self):
    return self.skill 

class Employee(models.Model):
  job_choices=(('0','Counter'),
                 ('1','Administrator'),
                 ('2','Economist'),
                 ('3','Developer'))
  first_name = models.CharField('Names', max_length=60)
  last_name = models.CharField('Lastnames', max_length=60)
  job=models.CharField('Job',max_length=1,choices=job_choices)
  departament = models.ForeignKey(Departament, on_delete=models.CASCADE)
  skill=models.ManyToManyField(Skill)
  SearchableFields=['first_name','last_name','job']

  class Meta:
    verbose_name='Empleo'
    verbose_name_plural='Empleos' 
    ordering=('last_name',) 
    unique_together=('first_name','last_name',)

  def __str__(self):
    for n,role in self.job_choices:
      if n==self.job:
        return f'{self.last_name}- {self.first_name} - {role}'

 