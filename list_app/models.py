from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    description = models.TextField()


class Address(models.Model):
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    house = models.IntegerField()
    flat = models.IntegerField()
    person = models.ForeignKey('Person', on_delete=models.PROTECT)


class Telephone(models.Model):
    number = models.CharField(max_length=12)
    type = models.CharField(max_length=32)
    person = models.ForeignKey('Person', on_delete=models.PROTECT)


class Email(models.Model):
    email = models.CharField(max_length=64)
    type = models.CharField(max_length=32)
    person = models.ForeignKey('Person', on_delete=models.PROTECT)


class Group(models.Model):
    name = models.CharField(max_length=64)
    person = models.ManyToManyField(Person)
