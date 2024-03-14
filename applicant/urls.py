from django.urls import path

from applicant import views
from applicant.views import applicants, delete_image
from grades.views import grade_list

app_name = "applicant"

urlpatterns = [
    path("applicants_list/", applicants, name="applicants"),
    path('<int:applicant_id>/', views.detail, name='detail'),
    path('<int:applicant_id>/modify/', views.modify, name='applicants_modify'),
    path('delete_image/<int:file_no>/', delete_image, name='delete_image'),
    path('register_grade/', views.register_grade, name='register_grade'),
    path("grade_list/", grade_list, name="grade_list"),
]