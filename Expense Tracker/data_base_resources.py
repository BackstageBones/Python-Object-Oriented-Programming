class SqlQueries():
    sql_create_expenses_table = """ CREATE TABLE IF NOT EXISTS Expenses (
                                            category varchar(255) PRIMARY KEY,
                                            quota float NOT NULL,
                                        ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer,
                                        status_id integer NOT NULL,
                                        project_id integer NOT NULL,
                                        begin_date text NOT NULL,
                                        end_date text NOT NULL,
                                        FOREIGN KEY (project_id) REFERENCES projects (id)
                                    );"""