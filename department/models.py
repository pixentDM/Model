from django.db import models

class Department(models.Model):
    department_id = models.IntegerField(verbose_name='부서 순번')
    department_name = models.CharField(verbose_name='부서 명')

    class Meta:
        db_table = '"public"."department"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return self.department_name



