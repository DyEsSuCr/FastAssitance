from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin
from .models import Business, UserProfile, EmployeeProfile, AdminProfile

# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
  list_display = ('name', 'address', 'phone_number', 'img_business')
  list_editable = ('img_business',)


class ProfileAdmin(UserAdmin):
  list_display = ('username', 'role')
  ordering = ['role']


class EmployeeProfileAdmin(UserAdmin):
  list_display = ('username', 'img_profile', 'role', 'user', 'business')
  list_editable = ('img_profile', 'user', 'business')
  ordering = ['business']


class AdminProfileAdmin(UserAdmin):
  list_display = ('username', 'img_profile', 'role', 'business')
  list_editable = ('img_profile', 'business')


admin.site.register(Permission)
admin.site.register(Business, BusinessAdmin)
admin.site.register(UserProfile, ProfileAdmin)
admin.site.register(EmployeeProfile, EmployeeProfileAdmin)
admin.site.register(AdminProfile, AdminProfileAdmin)