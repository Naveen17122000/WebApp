from django.contrib import admin
from . models import Employee,Deportment,person,Aadhar,EmployeeProxy


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empno','empname','salary','grade']
    list_editable=['empname']
    list_filter=['salary','deportment']

    def grade(self,rec):
        if rec.salary<250000:
            return 'Low'
        elif rec.salary<350000:
            return 'Medium'
        else:
            return 'High'

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Deportment)

admin.site.register(person)
admin.site.register(Aadhar)
admin.site.register(EmployeeProxy,EmployeeAdmin)