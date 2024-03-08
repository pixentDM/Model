from django.http import HttpResponse
from django.shortcuts import render, redirect

from applicant.models import Applicant
from grades.forms import GradesForm
from grades.models import Grades


def grade_list(request):
    all_grades = Grades.objects.select_related('applicant').all()
    return render(request, 'grades/grade_list.html', {'all_grades': all_grades})

def grade_detail(request, grade_id):
    grade = Grades.objects.select_related('applicant').get(pk=grade_id)
    return render(request, 'grades/grade_detail.html', {'grade': grade})

def grade_modify(request, grade_id):
    grade = Grades.objects.select_related('applicant').get(pk=grade_id)
    if request.method == 'POST':
        # 폼에서 전송된 데이터를 이용해 객체 업데이트
        form = GradesForm(request.POST, request.FILES, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade:grade_detail', grade_id=grade_id)

    else:
        # 기존의 객체 정보로 폼을 초기화
        form = GradesForm(instance=grade)

    context = {
        'form': form,
        'grade': grade
    }
    return render(request, 'applicant/applicants_modify.html', context)