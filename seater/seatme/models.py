from django.db import models


class Person(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    gender_choices = (('F', 'Female'), ('M', 'Male'), ('U', 'Not Specified'))
    gender = models.CharField(max_length=1, choices=gender_choices,
                              default='U')
    friends = models.ManyToManyField('self', blank=True, null=True)
    enemies = models.ManyToManyField('self', blank=True, null=True)


class Table(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    size = models.PositiveSmallIntegerField()
    layout_choices = (('R', 'Rectangle'),)
    layout = models.CharField(max_length=1, choices=layout_choices,
                              default='R')
