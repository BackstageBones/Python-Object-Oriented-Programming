import sqlite3
from sqlite3 import Error
import os

from data_base_resources import SqlQueries


class MyDataBase(object):

    def __init__(self, name= 'database.db'):
        """
        name: name of the database file
        """

        self.db_file = name
        self.conn = self.make_connection()

    def make_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            #print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                return conn

    def execute_query(self, *args):
        """ execute queries from sql statements
            :param args: sql statements
            :return:
            """
        for arg in args:
            try:
                self.conn.execute(arg)
            except Error as e:
                print(e)
        return self

if __name__ == "__main__":
    mydb = MyDataBase()
    mydb.make_connection()
    mydb.execute_query(SqlQueries.sql_create_expenses_table)