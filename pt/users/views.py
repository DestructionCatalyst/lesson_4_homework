from django.shortcuts import render
from django.http.response import JsonResponse, Http404
import os
from application.settings import TEMPLATE_DIR
from .models import Users


def index(request):
    user_list = Users.objects.all()
    return render(request,
                  os.path.join(TEMPLATE_DIR, 'users/index.html'),
                  {'title': 'All users', 'users': user_list})


def user_detail(request):
    try:
        user_id = request.GET.get('user_id')
        user = Users.objects.get(pk=user_id)
    except:
        raise Http404
    return JsonResponse({f'{user.username}': [f'{user.date_of_birth}',
                                              f'{user.address}',
                                              f'{user.phone}',
                                              f'{user.email}']})
