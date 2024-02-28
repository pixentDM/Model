from django.contrib import admin

from grades.models import Grades


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ['grade_id','firstStage_grade', 'secondStage_grade', 'applicant']
    # search_fields = ['firstStage_grade', 'secondStage_grade', 'applicant__applicant_name']