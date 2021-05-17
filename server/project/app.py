from flask import Flask, jsonify, request
from flask_cors import CORS
from uuid import uuid4

app = Flask(__name__)

CORS(app, resources={r'/*': { 'origins': '*'}})

BOOKS = [
    dict(
        id=uuid4().hex,
        title='On the Road',
        author='Jack Kerouac',
        read=True
    ),
    dict(
        id=uuid4().hex,
        title='Harry Potter and the Philosopher\'s Stone',
        author='JK Rowling',
        read=True
    ),
    dict(
        id=uuid4().hex,
        title='Green Eggs and Ham',
        author='Dr. Seuss',
        read=True
    )
]

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = dict(status='success')
    if request.method == 'POST':
        post_data = request.get_json()
        new_title = post_data.get('title')
        if len(list(filter(lambda book: book['title'] == new_title, BOOKS))) > 0:
            return jsonify(dict(status='error', message=f'Duplicate title "{new_title}"')), 500
        BOOKS.append(dict(
            id=uuid4().hex,
            title=new_title,
            author=post_data.get('author'),
            read=post_data.get('read')
        ))
        response_object['message'] = f'Book "{new_title}" added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        new_title = post_data.get('title')
        remove_book(book_id)
        BOOKS.append(dict(
            id=book_id,
            title=new_title,
            author=post_data.get('author'),
            read=post_data.get('read')
        ))
        response_object['message'] = f'Book "{new_title}" updated!'
    elif request.method == 'DELETE':
        title = remove_book(book_id)
        response_object['message'] = f'Book "{title}" removed!'
    else:
        book = [book for book in BOOKS if book['id'] == book_id]
        app.logger.info("%s", jsonify(book))
        if len(book) == 0:
            return jsonify(dict(status='error', message='Book not found')), 404

        response_object['book'] = book[0]
    return jsonify(response_object)

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            title = book['title']
            BOOKS.remove(book)
            return title
    return False

if __name__ == '__main__':
    app.run()
