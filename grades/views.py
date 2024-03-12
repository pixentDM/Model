from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect

from grades.forms import GradesForm
from grades.models import Grades


def grade_list(request):

    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어 가져오기
    search_field = request.GET.get('search_field', 'applicant__applicant_name')  # 검색 범위 가져오기
    error_message = ''

    query = Q()

    # 문자열 필드에 대한 검색 조건
    if kw:
        # 검색 범위에 따라 쿼리 구성
        if search_field == 'applicant__applicant_name':
            query |= Q(applicant__applicant_name__icontains=kw)
        elif search_field == 'applicant__unique_no':
            query |= Q(applicant__unique_no__icontains=kw)
        elif search_field == 'applicant__gender':
            query |= Q(applicant__gender__icontains=kw)
        elif search_field == 'applicant__nationality':
            query |= Q(applicant__nationality__icontains=kw)
        elif search_field == 'applicant__height':
            query |= Q(applicant__height__icontains=kw)
        elif search_field == 'applicant__weight':
            query |= Q(applicant__weight__icontains=kw)
        elif search_field == 'applicant__chest':
            query |= Q(applicant__chest__icontains=kw)
        elif search_field == 'applicant__waist':
            query |= Q(applicant__waist__icontains=kw)
        elif search_field == 'applicant__hips':
            query |= Q(applicant__hips__icontains=kw)
        elif search_field == 'applicant__languages':
            query |= Q(applicant__languages__icontains=kw)
        elif search_field == 'applicant__instagram_link':
            query |= Q(applicant__instagram_link__icontains=kw)
        elif search_field == 'firstStage_grade':
            query |= Q(firstStage_grade__icontains=kw)
        elif search_field == 'secondStage_grade':
            query |= Q(secondStage_grade__icontains=kw)
        elif search_field == 'nopass':
            query |= Q(nopass__icontains=kw)
        elif search_field == 'employee__users__username':
            query |= Q(employee__users__username__icontains=kw)


        # 날짜 필드에 대한 검색
        if search_field in ['birth_year']:
            try:
                search_date = datetime.strptime(kw, '%Y-%m-%d').date()

                date_filters = {
                    'birth_year': Q(birth_year=search_date),
                }
                query |= date_filters[search_field]
            except ValueError:
                error_message = '잘못된 날짜 형식입니다. YYYY-MM-DD 형식으로 입력해주세요.'
                all_grades = Grades.objects.none()  # 잘못된 날짜 형식으로 인한 빈 쿼리셋
                # 오류 메시지와 함께 컨텍스트를 생성하여 반환
                context = {
                    'all_grades': all_grades,
                    'page': page,
                    'kw': kw,
                    'search_field': search_field,
                    'error_message': error_message
                }
                return render(request, 'grades/grade_list.html', context)

    all_grades = Grades.objects.select_related('applicant', 'employee').filter(query).order_by('pk')

    print(f'Search Query: {query}')  # 콘솔에 검색 쿼리 출력
    print(f'Filtered Results: {Grades.objects.filter(query)}')  # 콘솔에 검색 결과 출력

    # 페이징 처리
    paginator = Paginator(all_grades, 15)  # 페이지당 15개씩 보여주기
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
        'all_grades': page_obj,
        'page': page,
    }

    return render(request, 'grades/grade_list.html', context)

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
            return redirect('grades:grade_detail', grade_id=grade_id)

    else:
        # 기존의 객체 정보로 폼을 초기화
        form = GradesForm(instance=grade)

    context = {
        'form': form,
        'grade': grade,
    }
    return render(request, 'grades/grade_modify.html', context)