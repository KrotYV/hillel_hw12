from django import forms


class Reminder(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(max_length=200)
    time = forms.DateTimeField()
