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

    def create_table(self, **kwargs):
        query = "CREATE TABLE IF NOT EXISTS {} ("
        comma = r', '
        for key, value in kwargs.items():
            if key != 'table_name':
                query = query + key + ' ' + value + comma
        query = query.format(kwargs['table_name']).rstrip(' ,') + ")"
        print(query)
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
        print(query)
        return self.cursor.execute(query)


db = MyDataBase('local')
db.create_table(table_name='store', item='TEXT', quantity='INTEGER', price='REAL')
#db.insert_values('store', 'wine glass', 8, 10.5)
