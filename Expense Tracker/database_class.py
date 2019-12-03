import sqlite3
from sqlite3 import Error

from .data_base_resources import SqlQueries


class MyDataBase(object):

    def __init__(self, path, name):
        """
        path: absolute path on your hard drive
        name: name of the database file
        """
        self.path = path
        self.db_file = name + '.db'
        self.queries = SqlQueries

    def make_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(r"{}".format(self.path) + r"\"" + self.db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                return conn

    def create_table(self):
        pass
