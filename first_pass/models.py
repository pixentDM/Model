from django.db import models

from applicant.models import Applicant
from grades.models import Grades


class First_pass(models.Model):
    first_id = models.IntegerField(verbose_name='순번')
    users = models.ForeignKey(Applicant, verbose_name='지원자 고유번호', on_delete=models.CASCADE)           # 지원자 현황 테이블 PK
    grades = models.ForeignKey(Grades, verbose_name='등급 순번', on_delete=models.CASCADE)                  # 등급 테이블 PK


    class Meta:
        db_table = '"public"."first_pass"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return self.users