from django import forms
from .models import Work

class workform(forms.ModelForm):
    class Meta:
        model=Work
        fields= ['title','description','file']