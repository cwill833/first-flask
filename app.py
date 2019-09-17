from flask import Flask, jsonify, request, Response
import json
from settings import *


books = [
    {
        "isbn": 34567890987654,
        "name": "The Cat In The Hat",
        "price": 7.99
    },
    {
        "isbn": 98765434567803,
        "name": "Green Eggs and Ham",
        "price": 6.99
    }
]

def v_request(obj):
    return True if ('name' in obj and 'price' in obj and 'isbn' in obj) else False

# GET /
@app.route('/')
def hello_world():
    return "Hello World!"

# GET /books
@app.route('/books')
def show_books():
    return jsonify({'books': books })

# GET /books/isbn
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price']
            }
    return jsonify(return_value)

# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    body = request.get_json()
    if v_request(body):
        new_book = {
            "name": body["name"],
            "price": body["price"],
            "isbn": body["isbn"]
        }
        books.append(new_book)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error": "invalid book object passed in request",
            "helpString": "Data passed in similar to this {'name':'bookname', 'price':'bookPrice, 'isbn': 'isbnOfBook'"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg), status=400, mimetype='application/json') # json.dumps is used to convert the object into json since that is what we are sending back
        return response

# PUT /books/isbn
@app.route('/books/<int:isbn>', methods=['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    book_update = {
        'name': request_data['name'],
        'price': request_data['price'],
        'isbn': isbn
    }
    i = 0
    for book in books:
        if book['isbn'] == isbn:
            books[i] = book_update
            break
        i += 1
    response = Response('', status=204)
    return response

# DELETE /books/isbn
@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    i = 0
    for book in books:
        if book['isbn'] == isbn:
            books.pop(i)
            return Response("", status=204)
        i += 1
    return Response('', status=404)





app.run(port=5000)