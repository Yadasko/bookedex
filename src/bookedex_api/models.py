from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.CharField(max_length=45, primary_key=True)
    name = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % (self.name)


class Author(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % (self.name)


class WrittenBy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.book.name, self.author.name)


class BookHunter(models.Model):
    username = models.CharField(max_length=45)

    def __str__(self):
        return "%s" % (self.username)


class CollectedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    hunter = models.ForeignKey(BookHunter, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.hunter.username, self.book.name)


class WantedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    hunter = models.ForeignKey(BookHunter, on_delete=models.CASCADE)

    def __str__(self):
        return "%s: %s" % (self.hunter.username, self.book.name)
