import json
from difflib import get_close_matches, SequenceMatcher


class InteractiveDictionary(object):
    def __init__(self):
        self.dictionary = json.load(open("data.json", "r"))

    def ask_for_key(self):
        while True:
            question = (input("type the key: "))
            if not question.isalpha():
                print("You have to provide a key word not a number")

            return question.lower()

    def search_data(self, question):
        try:
            self.dictionary[question]
        except KeyError:
            print(self.calculate_matches(question))
        else:
            print(self.dictionary[question])

    def calculate_matches(self, question):
        calculate_match = get_close_matches(question, self.dictionary.keys(), n=1)
        match_ratio = SequenceMatcher(None, question, calculate_match[0])
        if match_ratio.quick_ratio() > 0.8:
            print("Did you mean :", calculate_match, '?')
            user_input = input("Y/N ?").lower()
            if user_input in ('yes', 'y'):
                return self.dictionary[calculate_match[0]]
            else:
                pass
        else:
            return "No word definition found for that key, try again"

    def interface(self):
        while True:
            question = self.ask_for_key()
            self.search_data(question)


if __name__ == "__main__":
    dictionary = InteractiveDictionary()
    print(dictionary.interface())
