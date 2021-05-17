from project.app import app, BOOKS
from json import loads, dumps

def test_get_books():
    tester = app.test_client()
    response = tester.get('/books', content_type='application/json')
    assert response.status_code == 200
    parsed_response = loads(response.data)
    assert parsed_response['status'] == 'success'

def test_post_books():
    tester = app.test_client()
    data = dict(
        title='The Bare Romantic',
        author='Keats',
        read=False
    )
    response = tester.post('/books', data=dumps(data), content_type='application/json')
    assert response.status_code == 200
    parsed_response = loads(response.data)
    assert parsed_response['status'] == 'success'
    assert parsed_response['message'] == 'Book "The Bare Romantic" added!'

def test_post_duplicate():
    tester = app.test_client()
    data = dict(
        title='The Bare Romantic',
        author='Keats',
        read=False
    )
    tester.post('/books', data=dumps(data), content_type='application/json')
    response = tester.post('/books', data=dumps(data), content_type='application/json')
    assert response.status_code == 500
    parsed_response = loads(response.data)
    assert parsed_response['status'] == 'error'
    assert parsed_response['message'] == 'Duplicate title "The Bare Romantic"'

def test_get_book():
    tester = app.test_client()
    id = BOOKS[0]['id']
    response = tester.get(f'/books/{id}')
    assert response.status_code == 200

def test_get_not_found_book():
    tester = app.test_client()
    id = 'bad'
    response = tester.get(f'/books/{id}')
    assert response.status_code == 404

def test_update_book():
    tester = app.test_client()
    id = BOOKS[0]['id']
    data = dict(
        title='The Bare Romantic',
        author='Keats',
        read=False
    )
    response = tester.put(f'/books/{id}', data=dumps(data), content_type='application/json')
    assert response.status_code == 200
    parsed_response = loads(response.data)
    assert parsed_response['status'] == 'success'
    assert parsed_response['message'] == 'Book "The Bare Romantic" updated!'

def test_delete_book():
    tester = app.test_client()
    id = BOOKS[0]['id']
    title = BOOKS[0]['title']
    response = tester.delete(f'books/{id}')
    assert response.status_code == 200
    parsed_response = loads(response.data)
    assert parsed_response['status'] == 'success'
    assert parsed_response['message'] == f'Book "{title}" removed!'

def test_ping_pong():
    tester = app.test_client()
    response = tester.get('/ping', content_type='application/json')
    assert response.status_code == 200
    assert response.data == b'"pong!"\n'
