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
        for key, value in kwargs.items():
            if key != 'table_name':
                query = query + key + ' ' + value + " ,"
        query = query.replace(query[-1], '').format(kwargs['table_name']) +")"
        return self.cursor.execute(query)


db = MyDataBase('local')
print(db.create_table(table_name='store', item='TEXT', quantity='INTEGER', price='REAL'))
