from django.db import models

class Applicant(models.Model):
    unique_no = models.CharField(max_length=100, verbose_name='지원자 고유번호')
    applicant_name = models.CharField(max_length=50, verbose_name='지원자 명')
    # img = models.ImageField("이미지", upload_to="file", blank=True)
    gender = models.CharField(max_length=10, verbose_name='성별')
    nationality = models.CharField(max_length=3, verbose_name='국가')
    birth_year = models.DateField(verbose_name='생년월일')
    height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='키')  # ex)158.3
    weight = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='몸무게')
    chest = models.IntegerField(verbose_name='가슴 size')
    waist = models.IntegerField(verbose_name='허리 size')
    hips = models.IntegerField(verbose_name='엉덩이 size')
    languages = models.TextField(verbose_name='사용가능언어')
    instagram_link = models.URLField(verbose_name='인스타그램 링크')
    instagram_id = models.CharField(max_length=40, verbose_name='인스타그램 아이디')
    application_date = models.DateTimeField(verbose_name='지원일')
    application_day = models.CharField(max_length=7, verbose_name='지원일 순차')
    data_completion = models.DateTimeField(auto_now=False, verbose_name='데이터 백업일')
    data_check = models.DateTimeField(verbose_name='데이터 확인일자(매니저)')
    # charge = models.ForeignKey(employees, on_delete=models.CASCADE, verbose_name='담당자')
