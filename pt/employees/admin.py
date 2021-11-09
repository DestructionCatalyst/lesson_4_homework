from django.contrib import admin
from .models import Employees, Positions


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'position', 'phone', 'email',)
    list_display_links = ('name', 'date_of_birth',)
    search_fields = ('name', 'date_of_birth',)


admin.site.register(Employees, EmployeesAdmin)


class PositionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )
    search_fields = ('name', )


admin.site.register(Positions, PositionsAdmin)
