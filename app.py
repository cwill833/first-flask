from flask import Flask, jsonify, request, Response
from BookModel import *
from UserModel import User
from settings import *
from functools import wraps

import json, datetime, jwt

app.config['SECRET_KEY'] = 'rich'

@app.route('/login', methods=['POST'])
def get_token():
    request_data = request.get_json()
    username = str(request_data['username'])
    password = str(request_data['password'])

    match = User.username_password_match(username, password)

    if match:
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
        token = jwt.encode({'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
        return token
    else:
        return Response('', 401, mimetype='application/json')

def v_request(obj):
    return True if ('name' in obj and 'price' in obj and 'isbn' in obj) else False
def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
            return f(*args, **kwargs)
        except:
            return jsonify({'error': 'Need a valid token to view this page'}), 401
    return wrapper

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
@token_required
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
@token_required
def replace_book(isbn):
    request_data = request.get_json()
    Book.replace_book(isbn, request_data['name'], request_data['price'])
    response = Response('', status=204)
    return response

# DELETE /books/isbn
@app.route('/books/<int:isbn>', methods=['DELETE'])
@token_required
def delete_book(isbn):
    Book.delete_book(isbn)
    return Response('', status=204)





app.run(port=5000)