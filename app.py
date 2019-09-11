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

app.run(port=5000)