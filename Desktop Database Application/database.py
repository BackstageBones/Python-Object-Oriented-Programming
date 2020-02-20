"""
A class that stores basic  values about books such as author, year or unique identifying number
class creates a local db file at its instantiation and allows to insert, update or delete elements in it.
"""

import sqlite3


class MyDataBase(object):

    def __init__(self, db_name):
        self.db_name = db_name
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def __str__(self):
        return self.db_name

    def close_connection(self):
        self.connect.commit()
        return self.connect.close()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)"
        self.cursor.execute(query)
        return self.close_connection()

    def insert_values(self, title, author, year, isbn):
        query = f"INSERT INTO book VALUES (NULL, {title}, {author}, {year}, {isbn} )"
        self.cursor.execute(query)
        return self.close_connection()

    def view(self):
        query = "SELECT * FROM book"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_specific_row(self, row, item):
        query = "DELETE FROM book WHERE {}='{}'"
        query = query.format(row, item)
        self.cursor.execute(query)
        return self.close_connection()

    def update_table(self, title, author, year, isbn, id):
        query = f"UPDATE book SET title={title}, author={author}, year={year}, isbn={isbn} WHERE id={id}"
        self.cursor.execute(query)
        return self.close_connection()

    def search_table(self, title, author, year, isbn):
        query = f"SELECT * FROM book WHERE title={title} OR author={author} OR year={year} OR isbn={isbn}"
        self.cursor.execute(query)
        return self.cursor.fetchall()


