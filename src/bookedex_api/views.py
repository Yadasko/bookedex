from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from .serializers import BookSerializer, AuthorSerializer, CollectionSerializer
from .models import Book
from .models import Author
from .models import CollectedBook
# Create your views here.


def collection_list(request, hunter):

    if request.method == 'GET':
        collection = CollectedBook.objects.filter(
            hunter__username=hunter).prefetch_related('book')
        print(collection.query)
        print(collection)
        return JsonResponse(CollectionSerializer(collection, many=True).data, safe=False)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = CollectedBook.objects.all()
    serializer_class = CollectionSerializer
