# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import json
import requests
from Book import Book

app = Flask(__name__)

s = requests.Session()

API_KEY = ""
with open('./api_key.txt', 'r') as file:
    API_KEY = file.read()

URL = "https://www.googleapis.com/books/v1"
VOLUMES = f"{URL}/volumes"

books = []


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/isbn/<isbn>/')
def get_from_isbn(isbn):
    isbn = isbn.replace('-', '').strip()
    r = s.get(f"{VOLUMES}?q=isbn:{isbn}{API_KEY}")

    res = r.json()

    if "items" in res and len(res['items']) >= 1:
        for book in res['items']:
            b = Book.construct(json.dumps(book, indent=2))
            books.append(b)
            print(b.toString())
            return(b.toString())
    else:
        print("No books have been found with this ISBN..")
        return("No books have been found with this ISBN..")


if __name__ == "__main__":
    app.run(debug=True)
