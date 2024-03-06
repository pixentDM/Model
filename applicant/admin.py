from django.contrib import admin
from django.utils.html import format_html

from applicant.models import Applicant
from file.models import File


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = [
        'unique_no', 'applicant_name', 'gender', 'nationality', 'birth_year',
        'height', 'weight', 'chest', 'waist', 'hips', 'languages',
        'instagram_link', 'instagram_id', 'application_date',
        'application_day', 'data_completion', 'data_check','employee',
        'show_image'
    ]
    search_fields = ['applicant_name', 'nationality', 'languages']              # 검색 기능을 사용하기 위해 search_fields 속성 사용

    def show_image(self, obj):
        file = File.objects.filter(applicant=obj).first()
        if file and file.file_data:
            return format_html('<img src="{}" width="50" height="50"/>', file.file_data.url)
        return "-"

    show_image.short_description = 'Image'