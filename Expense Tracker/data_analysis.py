from database_class import MyDataBase
import pandas


class DataAnalysis(MyDataBase):
    def __init__(self, name):
        super().__init__(name)


    def display_data(self):
        df = pandas.read_sql_query("SELECT * FROM Expenses", self.db_file)
        return df


if __name__ == "__main__":
    Anal = DataAnalysis('database.db')
    Anal.display_data()
