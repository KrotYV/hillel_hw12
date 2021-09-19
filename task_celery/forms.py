from datetime import timedelta

from django import forms
from django.utils import timezone


class Reminder(forms.Form):
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=300)
    time = forms.DateTimeField(initial=timezone.now())

    def clean_eta(self):
        time = self.cleaned_data['time']
        if time < timezone.now():
            raise forms.ValidationError(f'The date must be later than {timezone.now()}')
        if time > timezone.now() + timedelta(days=2):
            raise forms.ValidationError(f'The date mustn\'t be later than {timezone.now() + timedelta(days=2)}')
        return time
