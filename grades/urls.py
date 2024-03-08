from django.urls import path

from grades import views

app_name = "grades"

urlpatterns = [
    path("grade_list/", views.grade_list, name="grade_list"),
    path('detail/<int:grade_id>/', views.grade_detail, name='grade_detail'),
    path('<int:applicant_id>/modify/', views.grade_modify, name='grade_modify'),
]