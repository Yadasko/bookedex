import json


# TODO: Use @property decorator to create getters and setters instead of attributes
# https://stackoverflow.com/a/41189407
class Book:

    def __init__(self, id, isbn, title, subtitle, authors):
        self.id = id
        self.isbn = isbn
        self.title = title
        self.subtitle = subtitle
        self.authors = authors

    @classmethod
    def construct(cls, json_string):
        try:
            data = json.loads(json_string)
        except:
            print("JSON could not be loaded")
            return cls("", "", "", "", [])

        vol_info = data['volumeInfo']

        ISBN_13 = next(
            d['identifier'] for d in vol_info['industryIdentifiers'] if d["type"] == "ISBN_13")

        subtitle = ""
        if "subtitle" in vol_info:
            subtitle = vol_info["subtitle"]
        return cls(data['id'], ISBN_13, vol_info['title'], subtitle, vol_info['authors'])

    def toString(self):
        return f"[Book instance@{self.id}] ISBN: {self.isbn} - Title: {self.title} - Subtitle: {self.subtitle} - Authors: {self.authors}"
