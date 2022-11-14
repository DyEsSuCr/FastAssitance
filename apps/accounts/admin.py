from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, EmployeeProfile, AdminProfile

# Register your models here.

class ProfileAdmin(UserAdmin):
  list_display = ('username', 'img_profile', 'role')
  list_editable = ('img_profile',)


class EmployeeProfileAdmin(UserAdmin):
  list_display = ('username', 'img_profile', 'role', 'user')
  list_editable = ('img_profile', 'user')


class AdminProfileAdmin(UserAdmin):
  list_display = ('username', 'img_profile', 'role')
  list_editable = ('img_profile',)


admin.site.register(Permission)
admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)
admin.site.register(AdminProfile, AdminProfileAdmin)