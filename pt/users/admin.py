from django.contrib import admin
from .models import Users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'date_of_birth', 'address', 'phone', 'email',)
    list_display_links = ('username', 'date_of_birth',)
    search_fields = ('username', 'date_of_birth',)


admin.site.register(Users, UsersAdmin)
