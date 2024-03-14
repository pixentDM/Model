from django.db import models

from applicant.models import Applicant
from employees.models import Employees


class Grades(models.Model):
    grade_id = models.AutoField(verbose_name='등급순번', primary_key=True)
    firstStage_grade = models.CharField(max_length=7, verbose_name='1차 등급', null=True, blank=True)
    secondStage_grade = models.CharField(max_length=7, verbose_name='2차 등급', null=True, blank=True)
    nopass = models.CharField(verbose_name='불합격', null=True, blank=True)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)              # 지원자 현황 테이블 PK
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)               # 직원 테이블 PK

    class Meta:
        db_table = '"public"."grades"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return f"{self.firstStage_grade}"

