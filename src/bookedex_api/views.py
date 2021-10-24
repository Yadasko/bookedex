from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import BookSerializer, AuthorSerializer, CollectionSerializer, CollectedBookData
from .models import Book
from .models import Author
from .models import CollectedBook
from .models import WantedBook
from .models import BookHunter

from .helpers.data_fetcher import *
from .helpers.api_outputs import *

from .wrappers.google_books import *


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
            else:
                return JsonResponse({'message': "You already have collected this book",
                                     'book': book}, safe=False)

        # TODO: Return json data with number of added books instead
        return JsonResponse(books, safe=False)


@api_view(["GET"])
def getCollectedBookInfo(request, hunter, book_id):

    book = CollectedBook.objects.filter(
        book__id=book_id, hunter__username=hunter)

    if not book.exists():
        return JsonResponse(createReturn(f"The book {book_id} is not known."), safe=False)

    return JsonResponse(CollectedBookData(book.first(), many=False).data, safe=False)


@api_view(["GET"])
def getBookFromISBN(request, hunter, ISBN):

    # 1. Check if book is already known
    #   if so, return it
    # 2. Retrieve from Google Books the data
    # 3. Check if book is in a wanted list or collected

    ISBN = ISBN.strip().replace('-', '')

    book = Book.objects.filter(ISBN_13=ISBN).first()

    if book == None:
        GBook = GoogleBooksWrapper()
        book = GBook.get_from_ISBN(ISBN)

        book = getBook(book)

    isCollected = False
    isWanted = False

    # Some data related to collection
    collectedAt = None

    collection = CollectedBook.objects.filter(
        book=book, hunter__username=hunter)

    wishlist = WantedBook.objects.filter(book=book, hunter__username=hunter)

    # Check if is in collection or wishlist
    if collection:
        isCollected = True
        collectedAt = collection.first().collectedAt

    if wishlist:
        isWanted = True

    result = BookSerializer(book, many=False).data
    result['collected'] = isCollected
    result['collectedAt'] = "N/A" if collectedAt == None else collectedAt
    result['wanted'] = isWanted

    return JsonResponse(result, safe=False)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = CollectedBook.objects.all()
    serializer_class = CollectionSerializer
