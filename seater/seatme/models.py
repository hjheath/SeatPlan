from django.db import models


class Person(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    GenderChoices = (('F', 'Female'), ('M', 'Male'), ('U', 'Not Specified'))
    gender = models.CharField(max_length=1, choices=GenderChoices, default='U')
    friends = models.ManyToManyField('self', blank=True, null=True)
    enemies = models.ManyToManyField('self', blank=True, null=True)


class Table(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    size = models.PositiveSmallIntegerField()
