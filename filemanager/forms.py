from django import forms
from django.forms import ClearableFileInput
from .models import File

class FileUpload(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }