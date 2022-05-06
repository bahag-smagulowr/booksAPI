from models import BookModel, ReviewModel
import psycopg2
from flask import current_app, g

book1 = BookModel('The Hobbit', 'J R R Tolkien', 1)
book2 = BookModel('The Lord of the Rings', 'J R R Tolkien', 2)
review1 = ReviewModel('a timeless classic', 1)
review2 = ReviewModel('I hated it', 1)
review3 = ReviewModel('an even more timeless classic', 2)
review4 = ReviewModel('I hated it even more', 2)




class Repository():
    def get_db(self):
        if 'db' not in g:
            g.db = current_app.config['pSQL_pool'].getconn()
        return g.db

    def books_get_all(self):
        
        conn = self.get_db()
        if (conn):
            ps_cursor = conn.cursor()
            ps_cursor.execute('SELECT title, author, bookId, cover from book ORDER BY title')
            book_records = ps_cursor.fetchall()
            book_list = []
            for row in book_records:
                book_list.append(BookModel(row[0], row[1], row[2], row[3]))
            ps_cursor.close()
        return book_list
    
    def get_book_by_id(self, book_id):
        books=[book1, book2]
        return next((x for x in books if x.bookId == book_id), None)
    
    def reviews_get_all(self):
        return [review1, review2, review3, review4]

    def get_review_by_id(self, book_id):
        reviews = [review1, review2, review3, review4]
        return [x for x in reviews if x.bookId == book_id]

    def review_add(self, data):
        return ReviewModel(data['content'], data['bookId'], 1)
    
    def book_add(self, data):
        conn = None
        try:
            conn = self.get_db()
            if (conn):
                ps_cursor = conn.cursor()
                ps_cursor.execute("insert into book(title,cover,author) values (%s, %s, %s) returning bookId", (data['title'], data['cover'], data['author']))
                conn.commit()
                id = ps_cursor.fetchone()[0]
                ps_cursor.close()
                book = BookModel(id, data['title'], data['cover'], data['author'])
            return book
        except Exception as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()