from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(Account)
class Account(UserAdmin):
    list_display = ['username','id','email','is_staff','first_name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('User Type'), {'fields': ('type', 'badge','badge_title')}),
        (('Extra Profile Builder'), {'fields': ('sex','dob','profile_pic','phone', 'other_info')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Story)
admin.site.register(EmergencyContact)
admin.site.register(AlertContact)
admin.site.register(Comment)
