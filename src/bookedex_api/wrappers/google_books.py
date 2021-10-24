import json
import requests


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class GoogleBooksWrapper():

    def __init__(self):
        self.URL = "https://www.googleapis.com/books/v1"
        self.VOLUMES = f"{self.URL}/volumes"
        self.session = requests.Session()

    def get_from_ISBN(self, ISBN):

        ISBN = ISBN.replace('-', '').strip()

        r = self.session.get(f"{self.VOLUMES}?q=isbn:{ISBN}")

        res = r.json()

        if "items" in res and len(res['items']) >= 1:
            book = res['items'][0]
            vol_info = book['volumeInfo']

            ISBN_13 = next(
                d['identifier'] for d in vol_info['industryIdentifiers'] if d["type"] == "ISBN_13")
            ISBN_13 = ISBN_13.strip().replace('-', '')

            book_dict = {}
            book_dict['id'] = book.get("id")
            book_dict['ISBN_13'] = ISBN_13
            book_dict['title'] = vol_info.get("title")
            book_dict['subtitle'] = vol_info.get("subtitle")
            book_dict['authors'] = vol_info.get("authors")

            return book_dict

        else:
            print("No books have been found with this ISBN..")
            return {}

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
