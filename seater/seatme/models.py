from django.db import models


class Person(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    male = models.NullBooleanField()
    friends = models.ManyToManyField('self')
    enemies = models.ManyToManyField('self')


class Table(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    size = models.PositiveSmallIntegerField()
