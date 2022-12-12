from django import forms
from .models import Grade

class GPAForm(forms.Form):
    sID = forms.CharField(max_length=10, required=True, label='Student ID')
    term = forms.IntegerField(required=True, label='Term')
    year = forms.IntegerField(required=True, label='Year')


class GPAModelForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['sID', 'term', 'year']
        label = {
            'sID': 'Student ID',
            'term': 'Term',
            'year': 'Year'
        }

class GPAHistoryModelForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['sID']
        label = {
            'sID': 'Student ID',
        }