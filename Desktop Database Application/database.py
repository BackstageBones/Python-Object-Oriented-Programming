"""
A class that stores basic  values about books such as author, year or unique identifying number
class creates a local db file at its instantiation and allows to insert, update or delete elements in it.
"""

import psycopg2


class MyDataBase(object):

    def __init__(self):
        self.connect = psycopg2.connect(
            dbname='tkinter_database',
            user='postgres',
            password='Logitechh151#',
            host='localhost',
            port='5432'
        )
        self.cursor = self.connect.cursor()
        self.create_table()

    # def __repr__(self):
    # return f"created database object named {self.db_name}"

    def __del__(self):
        self.close_connection()

    def commit_changes(self):
        return self.connect.commit()

    def close_connection(self):
        self.connect.commit()
        return self.connect.close()

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS book (id SERIAL PRIMARY KEY, title TEXT NOT NULL , author TEXT NOT NULL ,year INTEGER, isbn INTEGER) "
        self.cursor.execute(query)
        return self.commit_changes()

    def insert_values(self, title, author, year, isbn):
        query = "INSERT INTO book (id, title, author, year, isbn) VALUES (DEFAULT,'{}', '{}', {}, {})".format(title,
                                                                                                             author,
                                                                                                             year, isbn)
        self.cursor.execute(query)
        return self.commit_changes()

    def view(self):
        query = "SELECT * FROM book"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_specific_row(self, id):
        query = "DELETE FROM book WHERE id={}".format(id)
        self.cursor.execute(query)
        return self.commit_changes()

    def update_table(self, id, title, author, year, isbn):
        query = f"UPDATE book SET title={title}, author={author}, year={year}, isbn={isbn} WHERE id={id}"
        self.cursor.execute(query)
        return self.commit_changes()

    def search_table(self, title, author, year, isbn):
        query = f"SELECT * FROM book WHERE title='{title}' OR author='{author}' OR year='{year}' OR isbn='{isbn}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

