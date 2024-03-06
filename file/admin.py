from django.contrib import admin

from file.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = [
        'file_no','file_name','file_type','file_data','upload_date','is_active','applicant']

