from django.db import models

from applicant.models import Applicant
from progress.models import Progress


class Meeting(models.Model):
    meeting_no = models.IntegerField(verbose_name='미팅순번')
    meeting_name = models.CharField(verbose_name='미팅 명')
    meeting_schedule = models.DateTimeField(verbose_name='미팅 일정')
    meeting_type = models.CharField(verbose_name='미팅 유형')
    note = models.CharField(verbose_name='비고')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)              # 지원자 현황 테이블 PK
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE)                # 미팅 테이블 PK

    class Meta:
        db_table = '"public"."meeting"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return self.meeting_name