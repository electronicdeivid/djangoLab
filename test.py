'''class Empleado(models.Model):
    job_choices=(('0','Contador'),
                 ('1','Administrador'),
                 ('2','Economista'),
                 ('3','Developer'))
    #Modelo para tabla de empleado
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job=models.CharField('Trabajo',max_length=1,choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
#      for cargos in self.job_choices:  
 #      for n,cargo in cargos:
        for n,cargo in self.job_choices:
            if n==self.job:
             return f'{self.id}- {self.first_name} - {cargo}'

             '''
class Jobs():
    job_choices=(('0','Contador'),
                 ('1','Administrador'),
                 ('2','Economista'),
                 ('3','Developer'))

    for n,cargo in job_choices:
                print(f'{cargo}')  

    print(type(job_choices))            

