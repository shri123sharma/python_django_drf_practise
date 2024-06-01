from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(User, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


admin.site.register(Device, DeviceAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Task, TaskAdmin)
