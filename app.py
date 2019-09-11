from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        'name': 'The Cat In The Hat',
        'price': 7.99,
        'isbn': 34567890987654
    },
    {
        'name': 'Green Eggs and Ham',
        'price': 6.99,
        'isbn': 98765434567803
    }
]

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

app.run(port=5000)