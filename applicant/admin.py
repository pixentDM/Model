from django.contrib import admin

from applicant.models import Applicant


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "gender",
        "nationality",
        "birth_year",
    ]
