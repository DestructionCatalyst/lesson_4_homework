from django.urls import path

from employees.views import index, employee_detail, apply

urlpatterns = [
    path('', index, name='employee_list'),
    path('employee/', employee_detail, name='current_employee'),
    path('apply/', apply, name='apply')
]
