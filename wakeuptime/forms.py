from django import forms

class TimeForm(forms.Form):
    time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    
