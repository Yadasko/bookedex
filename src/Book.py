import json


class Book:

    def __init__(self, id, isbn_13, title, subtitle, authors):
        self.id = id

        if (len(isbn_13) != 13 or (not isbn_13.isdecimal())):
            raise ValueError("ISBN_13 must 13 of length and only numerals")

        self.isbn_13 = isbn_13
        self.title = title
        self.subtitle = subtitle

        print(type(authors))

        if not isinstance(authors, list):
            raise ValueError("Authors must be a list")

        self.authors = authors

    @classmethod
    def construct_from_dict(cls, data_dict):
        vol_info = data_dict['volumeInfo']

        ID = data_dict.get("id")
        ISBN_13 = next(
            d['identifier'] for d in vol_info['industryIdentifiers'] if d["type"] == "ISBN_13")
        ISBN_13 = ISBN_13.strip().replace('-', '')
        TITLE = vol_info.get("title")
        SUBTITLE = vol_info.get("subtitle")
        AUTHORS = vol_info.get("authors")

        return cls(id=ID, isbn_13=ISBN_13, title=TITLE,
                   subtitle=SUBTITLE, authors=AUTHORS)

    def __str__(self):
        return f"[Book instance@{self.id}] ISBN 13: {self.isbn_13} - Title: {self.title} - Subtitle: {self.subtitle} - Authors: {self.authors}"
