from django import forms

from .models import Trip, Trip_detail

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['trip']
        labels = {'trip': ''}

class HighlightsForm(forms.ModelForm):
    class Meta:
        model = Trip_detail
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
    