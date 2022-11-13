from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, EmployeeProfile

# Register your models here.

class ProfileAdmin(UserAdmin):
  list_display = ('username', 'img_profile', 'role')
  list_editable = ('img_profile','role')


class EmployeeProfileAmin(UserAdmin):
  list_display = ('username', 'img_profile', 'role')
  list_editable = ('img_profile','role')


admin.site.register(Permission)
admin.site.register(EmployeeProfile, EmployeeProfileAmin)
admin.site.register(UserProfile, EmployeeProfileAmin)