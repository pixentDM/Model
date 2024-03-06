from django.db import models

from department.models import Department
from position.models import Position
from users.models import Users


class Employees(models.Model):
    employee_id = models.CharField(verbose_name='직원 고유번호')
    start_date = models.DateField(verbose_name='입사일')
    users = models.ForeignKey(Users, verbose_name='사용자 고유번호', on_delete=models.CASCADE)           # 직원 테이블 PK
    position = models.ForeignKey(Position, verbose_name='직원 순번', on_delete=models.CASCADE)          # 직위 테이블 PK
    department = models.ForeignKey(Department, verbose_name='부서 순번', on_delete=models.CASCADE)      # 부서 테이블 PK

    class Meta:
        db_table = '"public"."employees"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return self.employee_id