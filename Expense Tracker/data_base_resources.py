class SqlQueries():
    sql_create_expenses_table = """ CREATE TABLE IF NOT EXISTS Expenses (
                                            id int NOT NULL,
                                            category varchar(255) PRIMARY KEY,
                                            quota float NOT NULL,
                                            date DATE NOT NULL
                                        ); """

    sql_insert_statement = ''' INSERT INTO Expenses(id, category, quota, date)
                                VALUES(?,?,?,?)
    
                             '''
