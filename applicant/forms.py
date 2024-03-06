from django import forms

from file.models import File
from .models import Applicant

class ApplicantForm(forms.ModelForm):

    image = forms.ImageField(label='Applicant Image', required=False)       # 이미지 업로드르 위한 파일 필드 추가

    def __init__(self, *args, **kwargs):            # unique_no 필드만 읽기전용
        super(ApplicantForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['unique_no'].disabled = True
    class Meta:
        model = Applicant
        fields = '__all__'

    def save(self, commit=True):
        instance = super(ApplicantForm, self).save(commit=False)

        if self.cleaned_data.get('image'):
            image = self.cleaned_data.get('image')                          # form에 제출된 이미지가 있을 경우 처리
            file_instance = File(file_name=image.name, file_data=image, applicant=instance)
            if commit:
                file_instance.save()

        if commit:
            instance.save()
        return instance