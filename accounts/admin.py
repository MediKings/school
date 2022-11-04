from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Profile


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personnal Info'), {'fields': ('post_name', 'first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (_('Importants dates'), {'fields': ('last_login', 'date_joined')}),
    )

    """For new User"""
    add_fieldsets =(
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    ) 
    list_display = ('username', 'first_name', 'last_name','email', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


admin.site.register(get_user_model(), CustomUserAdmin)
admin.site.register(Profile)
