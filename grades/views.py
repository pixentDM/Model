from django.shortcuts import render

from grades.models import Grades

def grade_list(request):
    all_grades = Grades.objects.select_related('applicant').all()
    return render(request, 'grades/grade_list.html', {'all_grades': all_grades})

def grade_detail(request, grade_id):
    grade = Grades.objects.select_related('applicant').get(pk=grade_id)
    return render(request, 'grades/grade_detail.html', {'grade': grade})