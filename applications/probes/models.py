from django.db import models

#---------- Create your models here.------------

class Prueba(models.Model):
    #Shields of my model
    titulo=models.CharField('Mes',max_length=30)
    subtitulo = models.CharField('Meta/s',max_length=50)
    #Functions of my model
    def __str__(self):
        return f'{self.titulo}: {self.subtitulo}'

