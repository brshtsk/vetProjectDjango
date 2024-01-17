# myapp/forms.py
from django import forms

class TextInputForm(forms.Form):
    text_input = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'custom-text-input-class'})
    )
