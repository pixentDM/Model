from django.db import models

class Position(models.Model):
    position_id = models.IntegerField(verbose_name='직위 순번')
    position_name = models.CharField(verbose_name='직위 명')

    class Meta:
        db_table = '"public"."position"'  # 스키마와 테이블 이름 지정

    def __str__(self):
        return self.position_name



