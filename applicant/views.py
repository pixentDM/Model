from django.shortcuts import render

from applicant.models import Applicant


def applicants(request):    # 오디션 지원자 현황
    """
    오디션 지원자 목록
    """
    applicants_list = Applicant.objects.order_by('-application_date')
    context = {'applicants_list': applicants_list}                           # applicants모델 데이터를 cotext변수에 저장
    return render(request, "applicant/applicants_list.html", context)

def detail(request, applicant_id):
    """
    오디션 지원자 상세 내용
    """
    applicant = Applicant.objects.get(id=applicant_id)
    context = {'applicant': applicant}
    return render(request, 'applicant/applicants_detail.html', context)