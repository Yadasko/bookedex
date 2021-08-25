from src.Book import Book
import pytest


def test_construct_from_valid_dict():

    ID = "abcdefgh"
    TITLE = "The Expanse"
    SUBTITLE = "Babylon's Ashes"
    AUTHORS = [
        "Daniel Abraham",
        "Ty Franck"
    ]
    ISBN_13 = "0987654321456"

    valid_dict = {
        "id": ID,
        "volumeInfo": {
            "title": TITLE,
            "subtitle": SUBTITLE,
            "authors": AUTHORS,
            "industryIdentifiers": [
                {
                    "type": "ISBN_9",
                    "identifier": "123456789"
                },
                {
                    "type": "ISBN_13",
                    "identifier": ISBN_13
                }
            ]
        }
    }
    book = Book.construct_from_dict(valid_dict)

    assert (book.id == ID and book.isbn_13 == ISBN_13 and book.title ==
            TITLE and book.subtitle == SUBTITLE and book.authors == AUTHORS)


def test_construct_from_invalid_dict_author():

    ID = "abcdefgh"
    TITLE = "The Expanse"
    SUBTITLE = "Babylon's Ashes"
    AUTHORS = "Daniel Abraham"
    ISBN_13 = "0987654321456"

    valid_dict = {
        "id": ID,
        "volumeInfo": {
            "title": TITLE,
            "subtitle": SUBTITLE,
            "authors": AUTHORS,
            "industryIdentifiers": [
                {
                    "type": "ISBN_9",
                    "identifier": "123456789"
                },
                {
                    "type": "ISBN_13",
                    "identifier": ISBN_13
                }
            ]
        }
    }
    with pytest.raises(ValueError):
        book = Book.construct_from_dict(valid_dict)


def test_construct_from_invalid_dict_isbn_13_short():

    ID = "abcdefgh"
    TITLE = "The Expanse"
    SUBTITLE = "Babylon's Ashes"
    AUTHORS = [
        "Daniel Abraham",
        "Ty Franck"
    ]
    ISBN_13 = "098765432142"

    valid_dict = {
        "id": ID,
        "volumeInfo": {
            "title": TITLE,
            "subtitle": SUBTITLE,
            "authors": AUTHORS,
            "industryIdentifiers": [
                {
                    "type": "ISBN_9",
                    "identifier": "123456789"
                },
                {
                    "type": "ISBN_13",
                    "identifier": ISBN_13
                }
            ]
        }
    }
    with pytest.raises(ValueError):
        book = Book.construct_from_dict(valid_dict)


def test_construct_from_invalid_dict_isbn_13_letter():

    ID = "abcdefgh"
    TITLE = "The Expanse"
    SUBTITLE = "Babylon's Ashes"
    AUTHORS = [
        "Daniel Abraham",
        "Ty Franck"
    ]
    ISBN_13 = "0987654z32142"

    valid_dict = {
        "id": ID,
        "volumeInfo": {
            "title": TITLE,
            "subtitle": SUBTITLE,
            "authors": AUTHORS,
            "industryIdentifiers": [
                {
                    "type": "ISBN_9",
                    "identifier": "123456789"
                },
                {
                    "type": "ISBN_13",
                    "identifier": ISBN_13
                }
            ]
        }
    }
    with pytest.raises(ValueError):
        book = Book.construct_from_dict(valid_dict)
