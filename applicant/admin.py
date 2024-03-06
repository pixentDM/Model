from django.contrib import admin

from applicant.models import Applicant

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = [
        'unique_no', 'applicant_name', 'gender', 'nationality', 'birth_year',
        'height', 'weight', 'chest', 'waist', 'hips', 'languages',
        'instagram_link', 'instagram_id', 'application_date',
        'application_day', 'data_completion', 'data_check','employee'
    ]
    search_fields = ['applicant_name', 'nationality', 'languages']              # 검색 기능을 사용하기 위해 search_fields 속성 사용
