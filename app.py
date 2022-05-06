from flask import Flask
from routes import Book, BookList, Review, ReviewList
from flask_restful import Api
from flask_cors import CORS
from flask import g
import os
from psycopg2 import pool

BASE_URL = '/api/bookreactions'
HOST = os.environ.get("HOST")
DATABASE = os.environ.get("DATABASE")
DB_PORT = os.environ.get("DB_PORT")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
MIN = os.environ.get("MIN")
MAX = os.environ.get("MAX")
DEBUG = os.environ.get("DEBUG")

app = Flask(__name__)
CORS(app)

api = Api(app)

app.config['pSQL_pool'] = pool.SimpleConnectionPool(MIN, MAX, user=USER, password=PASSWORD, host=HOST, port=DB_PORT, database=DATABASE)

api.add_resource(BookList, f'{BASE_URL}/Books')
api.add_resource(Book, f'{BASE_URL}/Books/<book_id>')
api.add_resource(ReviewList, f'{BASE_URL}/Reviews')
api.add_resource(Review, f'{BASE_URL}/Reviews/<book_id>')

@app.teardown_appcontext
def close_con(e):
    db = g.pop('db', None)
    if db is not None:
        app.config['pSQL_pool'].putconn(db)
        print('released connection back to pool')

if __name__ == '__main__':
    app.run(debug=DEBUG)
###