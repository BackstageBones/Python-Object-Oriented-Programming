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

    def create_table(self, tabel_name, **kwargs):
        query = "CREATE TABLE IF NOT EXISTS table.name ("
        for item in range(len(kwargs)):
            query = query + "{} {},"
        for key, value in kwargs.items():
            query.format(key, value)
        return query.replace('table.name', tabel_name) + """)")"""

    print(create_table('store', item='TEXT', quantity='INTEGER', price='REAL'))
