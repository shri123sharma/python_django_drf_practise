from django.db import models
# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Musician(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    instrument = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,)
    release_date = models.DateField()
    num_star = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    SHIRT_SIZE = {
        "S": "Small",
        "M": "Medium",
        "L": "Large"
    }
    name = models.CharField(max_length=255,)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)

    def __str__(self):
        return self.name

