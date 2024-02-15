from django.shortcuts import render

def applicants(request):    # 오디션 지원자 현황
    return render(request, "applicant/applicants_list.html")