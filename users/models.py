from django.db import models

from department.models import Department
from position.models import Position


class Users(models.Model):
    user_id = models.CharField(verbose_name='사용자 고유번호')
    username = models.CharField(verbose_name='사용자 명')
    password = models.CharField(verbose_name='비밀번호')
    email = models.CharField(verbose_name='이메일')
    phone = models.CharField(verbose_name='연락처')
    position = models.ForeignKey(Position, verbose_name='직원 순번', on_delete=models.CASCADE)          # 직위 테이블 PK
    department = models.ForeignKey(Department, verbose_name='부서 순번', on_delete=models.CASCADE)      # 부서 테이블 PK

    class Meta:
        db_table = '"public"."users"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return self.username

