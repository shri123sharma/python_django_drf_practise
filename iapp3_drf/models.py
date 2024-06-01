from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class FilmType(models.Model):
    film_type_name = models.CharField(max_length=2555, null=True)

    def __str__(self):
        return self.film_type_name


class Film(models.Model):
    film_name = models.CharField(max_length=200)
    film_type = models.ManyToManyField(FilmType)
    duration = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    release_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.film_name


class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    headquarters_location = models.CharField(max_length=100)
    is_large_company = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_name = models.CharField(max_length=255)
    launch_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.article_name


class Album(models.Model):
    name = models.CharField(max_length=255)
    launch_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class MusicTrack(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return self.title


class CustomManger(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(email="user1@gmail.com")


class Post(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, unique=True)

    objects = CustomManger()

    def __str__(self):
        return self.name+"-"+self.email
