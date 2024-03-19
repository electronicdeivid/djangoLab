from django.contrib import admin
from .models import Employee , Skill
#from .models import Skills
# Register your models here.
admin.site.register(Skill)


class EmployeeAdmin(admin.ModelAdmin):
 #   fields=[('first_name','last_name'),('job','departament'),'skill']
    #exclude=['departament']  #Para funcionar debo anular fields y vicebersa. lo mismo fieldsets
    actions_on_bottom = False
    actions_selection_counter = True
    list_display = ['first_name','last_name','job','departament']
    search_fields=Employee.SearchableFields
    list_filter=('job','skill','departament')
    filter_horizontal=('skill',)
    fieldsets = [
        (
            None,
            {
                "fields": [('first_name','last_name'),'job','departament'],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["skill"],
            },
        ),
    ]
   

admin.site.register(Employee, EmployeeAdmin)