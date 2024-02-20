from django.urls import path

from applicant import views
from applicant.views import applicants

app_name = "applicant"

urlpatterns = [
    path("applicants_list/", views.applicants, name="applicants"),
    path('<int:applicant_id>/', views.detail, name='detail'),
]