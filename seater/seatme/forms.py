from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'gender', 'friends', 'enemies')
        widgets = {
            'gender': forms.RadioSelect,
            'friends': forms.CheckboxSelectMultiple,
            'enemies': forms.CheckboxSelectMultiple,
        }
