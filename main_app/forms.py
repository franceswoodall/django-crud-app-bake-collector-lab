from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta: 
        model = Review
        fields = ['rating', 'date']

        widgets = {
            'date': forms.DateInput(
                attrs = {
                    'type': 'date'
                }
            ), 
            'rating': forms.RadioSelect(), 
            }
        