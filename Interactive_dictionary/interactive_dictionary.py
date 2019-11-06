import json
from difflib import get_close_matches, SequenceMatcher


class InteractiveDictionary(object):
    def __init__(self):
        self.dictionary = json.load(open("data.json", "r"))
        self.close_words = ('q', 'quit', 'end', '/')

    def ask_for_key(self):
        while True:
            question = (input("type the key: "))
            if not question.isalpha():
                return "You have to provide a key word not a number"
            return question

    def search_data(self, question):
        try:
            self.dictionary[question]
        except KeyError:
            return self.calculate_matches(question)
        else:
            return self.dictionary[question]

    def calculate_matches(self, question):

        if question.lower() in self.dictionary.keys():
            return self.dictionary[question.lower()]
        elif question.upper() in self.dictionary.keys():
            return self.dictionary[question.upper()]
        elif question.title() in self.dictionary.keys():
            return self.dictionary[question.title()]
        else:
            calculate_match = get_close_matches(question, self.dictionary.keys(), n=1)
            match_ratio = SequenceMatcher(None, question, calculate_match[0])
            if match_ratio.quick_ratio() > 0.8:
                print("Did you mean :", calculate_match, '?')
                user_input = input("Y/N ?").lower()
                if user_input in ('yes', 'y'):
                    return self.dictionary[calculate_match[0]]
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
    dictionary = InteractiveDictionary()
    print(dictionary.interface())
