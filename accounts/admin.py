from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
# Register your models here.

class CustomeUserAdmin(UserAdmin):
    model = User

    list_display = ('email','is_superuser','is_active')
    list_filter = ('email','is_superuser','is_active')
    searching_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
      ('Standard info', {
          'fields': ('email','password')
      }),
      ('Permissions', {
          'fields': ('is_staff', 'is_active','is_superuser')
      }),
      ('Group Permissions', {
          'fields': ('groups', 'user_permissions')
      }),
        ('Dates', {
          'fields': ('last_login',)
      }),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2','is_active','is_superuser','is_staff'),}),)

admin.site.register(User,CustomeUserAdmin)
admin.site.register(Profile)