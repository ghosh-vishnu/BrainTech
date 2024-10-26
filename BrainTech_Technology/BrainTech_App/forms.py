from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate_number', 'name', 'type', 'offer', 'issued', 'certificate_file']
