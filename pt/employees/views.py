from django.shortcuts import render
from django.http.response import JsonResponse, Http404, HttpResponseRedirect
import os
from application.settings import TEMPLATE_DIR
from .models import Employees, Positions
from .forms import ApplyForm
from django.urls import reverse
from django.views.decorators.http import require_http_methods, require_GET


def index(request):
    employees_list = Employees.objects.all()
    return render(request,
                  os.path.join(TEMPLATE_DIR, 'employees/index.html'),
                  {'title': 'All employees', 'employees': employees_list})


@require_GET
def employee_detail(request):
    try:
        employee_id = request.GET.get('employee_id')
        employee = Employees.objects.get(pk=employee_id)
    except:
        raise Http404
    return JsonResponse({f'{employee.name}': [f'{employee.date_of_birth}',
                                              f'{employee.position}',
                                              f'{employee.phone}',
                                              f'{employee.email}']})


@require_http_methods(['POST', 'GET'])
def apply(request):
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            new_employee = form.cleaned_data
            # decode numeric identifier to position name
            new_employee['position'] = Positions.objects.get(pk=new_employee['position']).name
            Employees(**new_employee).save()
            return HttpResponseRedirect(reverse('employee_list'))
    elif request.method == 'GET':
        form = ApplyForm()

    return render(request, os.path.join(TEMPLATE_DIR, 'employees/apply.html'), {'title': 'Work with us', 'my_form': form})
