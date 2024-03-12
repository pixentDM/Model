from django import forms

from file.models import File
from .models import Grades


class GradesForm(forms.ModelForm):

    GRADE_CHOICES = [
        ('', '----'),  # 기본 선택지
        ('S', 'S'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]
    PASS_CHOICES = [
        ('', '----'),  # 기본 선택지
        ('NO PASS', 'NO PASS'),
    ]

    firstStage_grade = forms.ChoiceField(choices=GRADE_CHOICES, required=False, label='1차 등급')
    secondStage_grade = forms.ChoiceField(choices=GRADE_CHOICES, required=False, label='2차 등급')
    nopass = forms.ChoiceField(choices=PASS_CHOICES, required=False, label='불합격 여부')

    class Meta:
        model = Grades
        exclude = ['image']
        labels = {
            'applicant': '지원자 명',
            'employee': '직원 명',
        }

    def save(self, commit=True):
        instance = super(GradesForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance