from django.contrib import admin

from department.models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'department_id','department_name']
