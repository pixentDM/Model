from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.dateparse import parse_date

from applicant.forms import ApplicantForm
from applicant.models import Applicant


def applicants(request):    # 오디션 지원자 현황
    """
    오디션 지원자 목록
    """

    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어 가져오기
    search_field = request.GET.get('search_field', 'applicant_name')  # 검색 범위 가져오기
    error_message = ''

    query = Q()

    # 문자열 필드에 대한 검색 조건
    if kw:
        # 검색 범위에 따라 쿼리 구성
        if search_field == 'applicant_name':
            query |= Q(applicant_name__icontains=kw)
        elif search_field == 'gender':
            query |= Q(gender__icontains=kw)
        elif search_field == 'nationality':
            query |= Q(nationality__icontains=kw)
        elif search_field == 'height':
            query |= Q(height__icontains=kw)
        elif search_field == 'weight':
            query |= Q(weight__icontains=kw)
        elif search_field == 'chest':
            query |= Q(chest__icontains=kw)
        elif search_field == 'waist':
            query |= Q(waist__icontains=kw)
        elif search_field == 'hips':
            query |= Q(hips__icontains=kw)
        elif search_field == 'languages':
            query |= Q(languages__icontains=kw)
        elif search_field == 'instagram_link':
            query |= Q(instagram_link__icontains=kw)
        elif search_field == 'instagram_id':
            query |= Q(instagram_id__icontains=kw)
        elif search_field == 'application_day':
            query |= Q(application_day__icontains=kw)


        # 날짜 필드에 대한 검색
        if search_field in ['birth_year', 'application_date', 'data_completion', 'data_check']:
            try:
                search_date = datetime.strptime(kw, '%Y-%m-%d').date()

                date_filters = {
                    'birth_year': Q(birth_year=search_date),
                    'application_date': Q(application_date__date=search_date),
                    'data_completion': Q(data_completion__date=search_date),
                    'data_check': Q(data_check__date=search_date),
                }
                query |= date_filters[search_field]
            except ValueError:
                error_message = '잘못된 날짜 형식입니다. YYYY-MM-DD 형식으로 입력해주세요.'
                applicants_list = Applicant.objects.none()  # 잘못된 날짜 형식으로 인한 빈 쿼리셋
                # 오류 메시지와 함께 컨텍스트를 생성하여 반환
                context = {
                    'applicants_list': applicants_list,
                    'page': page,
                    'kw': kw,
                    'search_field': search_field,
                    'error_message': error_message
                }
                return render(request, 'applicant/applicants_list.html', context)

    # 데이터 정렬(데이터 백업일_내림차순 => 지원일_오름차순 => 지원자 고유번호_오름차순)
    # applicants_list = Applicant.objects.filter(query).order_by('-data_completion__date', 'application_date',
    #                                                           'unique_no').distinct()
    applicants_list = Applicant.objects.filter(query).prefetch_related('file_set').order_by('-data_completion__date',
                                                                                            'application_date',
                                                                                            'unique_no').distinct()

    # 페이징 처리
    paginator = Paginator(applicants_list, 15)  # 페이지당 15개씩 보여주기
    try:
        page = int(page)  # 문자열을 정수로 변환
    except ValueError:
        page = 1  # 변환에 실패한 경우 첫 번째 페이지로 설정

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)  # 페이지 번호가 정수가 아닌 경우 첫 페이지
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)  # 페이지 범위를 벗어난 경우 마지막 페이지

    context = {
        'applicants_list': page_obj,
        'page': page,
        'kw': kw,
        'search_field': search_field,
        'error_message': error_message  # 오류 메시지 포함
    }
    return render(request, 'applicant/applicants_list.html', context)

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
        form = ApplicantForm(request.POST, request.FILES, instance=applicant)
        if form.is_valid():
            form.save()
            return redirect('applicant:detail', applicant_id=applicant_id)

    else:
        # 기존의 객체 정보로 폼을 초기화
        form = ApplicantForm(instance=applicant)

    context = {
        'form': form,
        'applicant': applicant
    }
    return render(request, 'applicant/applicants_modify.html', context)
