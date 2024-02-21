from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):            # unique_no 필드만 읽기전용
        super(ApplicantForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['unique_no'].disabled = True
    class Meta:
        model = Applicant
        fields = '__all__'
