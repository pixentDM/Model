from django.db import models

from applicant.models import Applicant
from grades.models import Grades


class Second_pass(models.Model):
    second_id = models.IntegerField(verbose_name='순번')
    users = models.ForeignKey(Applicant, verbose_name='지원자 고유번호', on_delete=models.CASCADE)           # 지원자 현황 테이블 PK
    grades = models.ForeignKey(Grades, verbose_name='등급 순번', on_delete=models.CASCADE)                  # 등급 테이블 PK

    class Meta:
        db_table = '"public"."second_pass"'  # 스키마와 테이블 이름 지정



