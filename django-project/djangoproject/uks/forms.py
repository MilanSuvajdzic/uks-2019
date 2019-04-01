from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from .models import Milestone


class DateInput(forms.DateInput):
    input_type = 'date'


class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': DatePickerInput(format='%d-%m-%Y'), # default date-format %m/%d/%Y will be used
            'end_date': DatePickerInput(format='%d-%m-%Y'), # specify date-frmat
        }