from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
  readonly_fields = ('created_at',)
  list_display = ('username', 'img_profile', 'is_admin',)
  list_editable = ('img_profile', 'is_admin',)


admin.site.register(Permission)
admin.site.register(User, CustomUserAdmin)