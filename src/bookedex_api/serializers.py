from rest_framework import serializers
from .models import Book
from .models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('name', )


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'authors', 'ISBN_13')
