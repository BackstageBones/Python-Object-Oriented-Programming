import sqlite3
from sqlite3 import Error


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


    def create_table(self, querie):
        """ create a table from the sql statement
            :param querie: create table statement
            :return: db file
            """
        try:
            self.conn.execute(querie)
        except Error as e:
            print(e)
        return self.db_file

    def insert_data(self, statement, data):
        """ inserts data into selected table
            :param statement: existing sql table
            :param data -> tuple: values you wish to insert inside table
            :return: updated sql table
        """
        try:
            self.conn.execute(statement, data)
        except Error as e:
            print(e)
        else:
            self.conn.close()
        return self





if __name__ == "__main__":
    mydb = MyDataBase()
    mydb.make_connection()
    mydb.create_table(SqlQueries.sql_create_expenses_table)
    mydb.insert_data(SqlQueries.sql_insert_statement, (1,'food', 300, 11-12.2019))