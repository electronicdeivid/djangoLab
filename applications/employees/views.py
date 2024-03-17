
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Employee , Skill

# Create your views here.
class IndexView(TemplateView):
    template_name='home.html'

class EmployeeListView(ListView):
    model= Employee
    template_name='employee.html'
    context_object_name='employee'

    def mostrar_empleado(request):
        employee_rol=Employee.objects.first()
        return render(request,'employee.html',{'employee_rol': employee_rol})

# 1.- Listar todos los empleados
'''

'''
# 2.- Listar todos los empleados que pertenecen a un área de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado

    