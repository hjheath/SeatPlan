from django.shortcuts import render
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


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            person = Person(name=form.cleaned_data['name'])
            person.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()
    persons = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'persons': persons})


def clear(request):
    Person.objects.all().delete()
    form = PersonForm()
    persons = Person.objects.all()
    return render(request, 'index.html', {'form': form, 'persons': persons})
