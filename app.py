from flask import Flask, jsonify, request

app = Flask(__name__)


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
        return "True"
    else:
        return "False"


app.run(port=5000)