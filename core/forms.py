from django import forms

class EventForm(forms.Form):
    name = forms.CharField(label='Event name', max_length=256)