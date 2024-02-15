from django.urls import path

from applicant.views import applicants

urlpatterns = [
    path("applicants_list/", applicants),
]