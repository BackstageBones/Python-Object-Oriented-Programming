from difflib import get_close_matches

import mysql.connector


class MySqlInteractiveDictionary(object):
    def __init__(self):
        self._connection = mysql.connector.connect(
            user="ardit700_student",
            password="ardit700_student",
            host="108.167.140.122",
            database="ardit700_pm1database"
        )

        self._cursor = self._connection.cursor(())
        self.close_words = ('q', 'quit', 'end', '/')

    def ask_for_key(self):
        while True:
            question = (input("type the key: "))
            if not question.isalpha():
                return "You have to provide a key word not a number"
            return question

    def search_data(self, question):
        question_variants = [question.lower(), question.upper(), question.title()]
        query = "SELECT * FROM Dictionary WHERE Expression = '{}'"

        for variants in question_variants:
            self._cursor.execute(query.format(variants))
            results = self._cursor.fetchall()
            if results:
                return [result for result in results]
            else:
                self.calculate_matches(question)
                break

    def calculate_matches(self, question):
        self._cursor.execute("SELECT * FROM Dictionary")
        row = [item[0] for item in self._cursor.fetchall()]
        calculate_match = get_close_matches(question, row)
        print("Did you mean :", calculate_match[0], '?')
        user_input = input("Y/N ?").lower()
        if user_input in ("yes","y"):
            self._cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(calculate_match[0]))
            print(self._cursor.fetchall())
        else:
            return "No word definition found for that key, try again"

    def interface(self):
        while True:
            question = self.ask_for_key()
            if question in self.close_words:
                break
            else:
                print(self.search_data(question))


if __name__ == "__main__":
    dictionary = MySqlInteractiveDictionary()
    print(dictionary.interface())
