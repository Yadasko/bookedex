from bookedex_api.models import Book, Author, CollectedBook, BookHunter


def createBook(book_data):
    """
    Takes a dict and creates a book from it's values
    It matches the Book fields to the dict keys
    """

    authors = [getAuthorByName(author) for author in book_data['authors']]

    # We remove these fields because they are manytoone/manytomany relationship
    # fields and we either need to handle them directly or just don't care about them
    field_blacklist = [
        'collectedbook',
        'wantedbook',
        'authors'
    ]

    # We delete collectedbook and wantedbook as they are manytoone relationship fields
    allowed_fields = [field.name for field in Book._meta.get_fields() if not (
        field.name in field_blacklist)]

    book_data = {key: value for (
        key, value) in book_data.items() if key in allowed_fields}

    b = Book(**book_data)
    b.save()
    b.authors.set(authors)
    return b


def getBook(book):
    """
    Takes a dict with all the book data in it
    Uses the id to find if we already know it
    """
    book_instance = Book.objects.filter(id=book['id'])

    if book_instance.exists():
        return book_instance.first()

    else:
        book_instance = createBook(book)

    return book_instance


def getAuthorByName(name):
    author, created = Author.objects.get_or_create(name=name)
    return author


def isAlreadyCollected(hunter, book):
    return CollectedBook.objects.filter(book=book, hunter=hunter).exists()
