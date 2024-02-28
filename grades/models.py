from django.db import models

from applicant.models import Applicant


class Grades(models.Model):
    grade_id = models.IntegerField(verbose_name='등급순번')
    firstStage_grade = models.CharField(max_length=7, verbose_name='1차 등급')
    secondStage_grade = models.CharField(max_length=7, verbose_name='2차 등급')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)              # 지원자 현황 테이블 FK

    def __str__(self):
        return self.firstStage_grade