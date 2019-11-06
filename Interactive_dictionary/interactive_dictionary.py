import json


class InteractiveDictionary(object):
    def __init__(self):
        self.dictionary = json.load(open("data.json", "r"))

    def ask_for_key(self):
        while True:
            question = (input("type the key: "))
            if not question.isalpha():
                print("You have to provide a key word not a number")
                break

            return question.lower()

    def search_data(self):
        question = self.ask_for_key()
        while True:
            try:
                print(self.dictionary[question])
            except KeyError:
                print("No word definition found for that key, try again")
                break
            else:
                break

    def interface(self):
        while True:
            self.ask_for_key()
            self.search_data()


if __name__ == "__main__":
    dictionary = InteractiveDictionary()
    dictionary.interface()
