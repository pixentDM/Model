from django.contrib import admin

from employees.models import Employees


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = [
        'employee_id','start_date','users','position','department']
    # search_fields = ['applicant_name', 'nationality', 'languages']              # 검색 기능을 사용하기 위해 search_fields 속성 사용
