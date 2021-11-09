from django.urls import path

from users.views import index, user_detail

urlpatterns = [
    path('', index, name='user_list'),
    path('user/', user_detail, name='current_user'),
]