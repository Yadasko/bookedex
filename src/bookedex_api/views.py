from django.shortcuts import render
from rest_framework import viewsets

from .serializers import BookSerializer, AuthorSerializer
from .models import Book
from .models import Author
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
