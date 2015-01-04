from django.shortcuts import render

from .models import Person
from .forms import PersonForm


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
            person = Person(name=form.cleaned_data['name'],
                            gender=form.cleaned_data['gender'])
            person.save()
            friends = form.cleaned_data['friends']
            enemies = form.cleaned_data['enemies']
            for enemy in enemies:
                person.enemies.add(enemy)
            for friend in friends:
                person.friends.add(friend)
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
