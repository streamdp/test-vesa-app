from django import forms
from .models import Fan


class QueryForm(forms.Form):
    airflow = forms.IntegerField(label='AIRFLOW', widget=forms.TextInput(attrs={'class': 'form-control'}))
    airflow_unit = forms.ChoiceField(label='UNIT', required=True, widget=forms.Select(attrs={'class': 'form-control'}),
                                     choices=Fan.AIRFLOW_UNIT_CHOICES)
    pressure = forms.IntegerField(label='TOTAL PRESSURE', widget=forms.TextInput(attrs={'class': 'form-control'}))
    pressure_unit = forms.ChoiceField(label='UNIT', required=True, widget=forms.Select(attrs={'class': 'form-control'}),
                                      choices=Fan.PRESSURE_UNIT_CHOICES)