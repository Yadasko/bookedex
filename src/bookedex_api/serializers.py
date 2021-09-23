from rest_framework import serializers
from .models import Book
from .models import Author
from .models import CollectedBook


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('name', )


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'authors', 'ISBN_13')


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollectedBook
        fields = ('hunter', 'book')

    book = BookSerializer(many=False)
