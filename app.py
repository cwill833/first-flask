from flask import Flask, jsonify, request, Response
from BookModel import *
from settings import *
import json
from settings import *

def v_request(obj):
    return True if ('name' in obj and 'price' in obj and 'isbn' in obj) else False

# GET /
@app.route('/')
def hello_world():
    return "Hello World!"

# GET /books
@app.route('/books')
def show_books():
    return jsonify({'books': Book.get_all_books() })

# GET /books/isbn
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = Book.get_book(isbn)
    return jsonify(return_value)

# POST /books
@app.route('/books', methods=['POST'])
def add_book():
    body = request.get_json()
    if v_request(body):
        Book.add_book(body["name"], body["price"], body["isbn"])
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(body['isbn'])
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
    Book.replace_book(isbn, request_data['name'], request_data['price'])
    response = Response('', status=204)
    return response

# DELETE /books/isbn
@app.route('/books/<int:isbn>', methods=['DELETE'])
def delete_book(isbn):
    Book.delete_book(isbn)
    return Response('', status=204)





app.run(port=5000)