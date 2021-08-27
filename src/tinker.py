from Book import Book
import requests
import json

s = requests.Session()

API_KEY = ""
with open('./api_key.txt', 'r') as file:
    API_KEY = file.read()

URL = "https://www.googleapis.com/books/v1"
VOLUMES = f"{URL}/volumes"
isbn = "9791035501952"

r = s.get(f"{VOLUMES}?q=isbn:{isbn}{API_KEY}")

res = r.json()

if "items" in res and len(res['items']) >= 1:
    for book in res['items']:
        b = Book.construct_from_dict(book)
        print(b)
