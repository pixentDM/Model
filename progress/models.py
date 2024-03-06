from django.db import models

from applicant.models import Applicant


class Progress(models.Model):
    progress_no = models.IntegerField(verbose_name='진행현황 순번')
    no_response = models.CharField(verbose_name='미응답자')
    notified = models.CharField(verbose_name='통보된 자')
    schedule_coordination = models.CharField(verbose_name='일정 조율')
    schedule_confirmed = models.CharField(verbose_name='일정 확정')
    schedule_confirmedday = models.TimeField(verbose_name='일정 확정일')
    applicant = models.ForeignKey(Applicant, verbose_name='지원자 고유번호', on_delete=models.CASCADE)              # 지원자 현황 테이블 PK

    class Meta:
        db_table = '"public"."progress"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return self.applicant