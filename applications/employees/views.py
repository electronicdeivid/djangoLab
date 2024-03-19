
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Employee , Skill
#from applications.departament.models import Departament

# Create your views here.
class IndexView(TemplateView):
    template_name='home.html'


class EmployeeListView(ListView):
    model= Employee
    context_object_name='employee'
    template_name='employee.html'


class EmployeeAreaListView(ListView):
    model=Employee
    context_object_name='employee'
    template_name='areaemployee.html'
    




# 1.- Listar todos los empleados
# 2.- Listar todos los empleados que pertenecen a un área de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado

    