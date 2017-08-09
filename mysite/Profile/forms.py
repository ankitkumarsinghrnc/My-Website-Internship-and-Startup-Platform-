from django import forms
from Profile.models import entries

class entriesForm(forms.ModelForm):

    class Meta:
        model = entries
        fields = ['name','enrollment','date_of_birth','skills','more_about_you','image']
