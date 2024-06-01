from rest_framework import serializers
from .models import UserProfile, Book, FilmType, Film, Company, Article, Album


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'bio', 'date_of_birth')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_year')


class FilmTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmType
        fields = ['id', 'film_type_name']


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'film_type', 'duration', 'release_date', 'film_name']


class BasicCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'industry']


class DetailedCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'industry',
                  'headquarters_location', 'is_large_company']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
