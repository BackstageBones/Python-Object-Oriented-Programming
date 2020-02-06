import sqlite3
import logging


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

    def create_table(self, **kwargs):
        """
         param kwargs: create arbitrary number of columns inside your table
         param table_name: first parameter must be specified with table_name which creates table
        """
        query = "CREATE TABLE IF NOT EXISTS {} ("
        comma = r', '
        for key, value in kwargs.items():
            if key != 'table_name':
                query = query + key + ' ' + value + comma
        query = query.format(kwargs['table_name']).rstrip(' ,') + ")"
        return self.cursor.execute(query)


    def insert_values(self, *args):
        query = r"INSERT INTO {} VALUES ("
        comma = r','
        for arg in args:
            if arg != args[0]:
                if type(arg) == str:
                    query = query + "'" + arg + "'" + comma
                else:
                    query = query + str(arg) + comma
        query = query.format(args[0]).rstrip(" ,") + ")"
        return self.cursor.execute(query)


    def view(self, table_name):
        self.cursor.execute("SELECT * FROM {}".format(table_name))
        return self.cursor.fetchall()


    def delete_specific_row(self, table_name, row, item):
        query = "DELETE FROM {} WHERE {}='{}'"
        query = query.format(table_name, row, item)
        self.cursor.execute(query)

    def update_table(self, **kwargs):
        query = "UPDATE {} SET "
        query_ending = " WHERE {}={}"
        comma = r', '
        for key, value in kwargs.items():
            if key != 'table_name':
                if key != 'item':
                    query = query + str(key) + '=' + str(value) + comma
                else:
                    query = query.format(kwargs['table_name']).rstrip(" ,") + query_ending.format(key,"'" + value+"'")
        return self.cursor.execute(query)




db = MyDataBase('local')
db.create_table(table_name='store', item='TEXT', quantity='INTEGER', price='REAL')
db.insert_values('store', 'wine glass', 8, 10.5)
#db.delete_specific_row('store','item', "wine glass")
db.update_table(table_name='store', quantity=10, price=15, item='coffe cup')
print(db.view('store'))
