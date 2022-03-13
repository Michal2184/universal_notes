from django import forms

class EmailForm(forms.Form):
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)