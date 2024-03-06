from django.db import models

from applicant.models import Applicant


class File(models.Model):
    file_no = models.IntegerField(verbose_name='파일고유번호')
    file_name = models.CharField(verbose_name='파일 명')
    file_type = models.CharField(verbose_name='타입')
    file_data = models.FileField(upload_to='uploads/', verbose_name='파일 데이터 저장')
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name='업로드 날짜')
    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)              # 지원자 현황 테이블 PK

    class Meta:
        db_table = '"public"."file"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return self.file_name