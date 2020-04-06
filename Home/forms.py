from django import forms

class NameForm(forms.Form):
    sarcasm = forms.CharField(label='Enter Text', max_length=500)