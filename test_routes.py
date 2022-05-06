from models import BookModel, ReviewModel
from routes import Review, ReviewList, Book, BookList
from repository import Repository
from unittest.mock import MagicMock
from flask import request
from app import app

book1 = BookModel('test The Hobbit', 'J R R Tolkien', 1)
book2 = BookModel('test The Lord of the Rings', 'J R R Tolkien', 2)
review1 = ReviewModel('test a timeless classic', 1)
review2 = ReviewModel('test I hated it', 1)
review3 = ReviewModel('test an even more timeless classic', 2)
review4 = ReviewModel('test I hated it even more', 2)

def test_booklist_get():
    repo = MagicMock(spec=Repository)
    repo.books_get_all.return_value = [book1, book2]
    books = BookList(repo).get()
    assert books[0]['bookId'] == 1
    assert books[1]['title'] == 'test The Lord of the Rings'

def test_booklist_post():
    with app.test_request_context():
        repo = MagicMock(spec=Repository)
        req = MagicMock(spec=request)
        data = BookModel('Elementary', 'Kevin Rattan')
        req.json.return_value = data.__dict__
        repo.book_add.return_value = BookModel('Elementary', 'Kevin Rattan', 100)
        book = BookList(repo).post(req)
        assert int(book['bookId']) == 100
        assert book['title'] == 'Elementary'
        assert book['author'] == 'Kevin Rattan'