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
        fields = ('id', 'title', 'subtitle', 'authors', )


class BookSerializerWithoutAuthor(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', )


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CollectedBook
        fields = ('book', )

    book = BookSerializerWithoutAuthor(many=False)
