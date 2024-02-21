from django.shortcuts import render, get_object_or_404, redirect

from applicant.forms import ApplicantForm
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
    applicant = get_object_or_404(Applicant, id=applicant_id)
    context = {'applicant': applicant}
    return render(request, 'applicant/applicants_detail.html', context)

def modify(request, applicant_id):
    """
    오디션 지원자 정보 수정
    """
    applicant = get_object_or_404(Applicant, id=applicant_id)
    if request.method == 'POST':
        # 폼에서 전송된 데이터를 이용해 객체 업데이트
        form = ApplicantForm(request.POST, instance=applicant)
        if form.is_valid():
            form.save()
            # return redirect('applicants')  # 목록 페이지로 리다이렉트
            return redirect('applicant:detail', applicant_id=applicant_id)

    else:
        # 기존의 객체 정보로 폼을 초기화
        form = ApplicantForm(instance=applicant)
    return render(request, 'applicant/applicants_modify.html', {'form': form, 'applicant': applicant})
