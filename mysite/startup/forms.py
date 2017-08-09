from django import forms
from startup.models import startups

class startupForm(forms.ModelForm):

    class Meta:
        model = startups
        fields = ['company_name','co_founders','details','logo']
