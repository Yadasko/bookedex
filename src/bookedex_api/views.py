from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import BookSerializer, AuthorSerializer, CollectionSerializer
from .models import Book
from .models import Author
from .models import CollectedBook
from .models import BookHunter

from .helpers.data_fetcher import *


# TODO: Find out difference between functions and classes in views
@api_view(["GET", "POST"])
def collection_list(request, hunter):

    if request.method == 'GET':
        collection = CollectedBook.objects.filter(
            hunter__username=hunter).prefetch_related('book')
        return JsonResponse(CollectionSerializer(collection, many=True).data, safe=False)

    elif request.method == 'POST':
        body = request.data

        if not "books" in body or not type(body['books']) is list:
            # TODO: Return true error page with associated HTTP error code
            return JsonResponse("POST body is missing 'books' array", safe=False)

        hunter_instance = BookHunter.objects.filter(
            username=hunter).first()

        books = body['books']
        for book in books:
            book_instance = getBook(book)

            if not isAlreadyCollected(hunter_instance, book_instance):
                CollectedBook.objects.create(
                    book=book_instance, hunter=hunter_instance)

        # TODO: Return json data with number of added books instead
        return JsonResponse(books, safe=False)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = CollectedBook.objects.all()
    serializer_class = CollectionSerializer
