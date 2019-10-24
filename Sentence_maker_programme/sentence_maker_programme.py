class MakeSentence(object):

    def __init__(self):
        self.simple_list = []
        self.interrogatives = ('who', 'where', 'why', 'how')

    def ask_for_sentence(self):
        for i in range(0, 3):
            try:
                question = str(input("Provide a sentence"))
            except ValueError:
                print("You must provide a sentence not a number")
            else:
                if question == '/end':
                    break
                else:
                    self.simple_list.append(question)

    def format_sentence(self):
        for word in self.simple_list:
            if word.startswith(self.interrogatives):
                self.simple_list[self.simple_list.index(word)] = word + " ?"
            else:
                self.simple_list[self.simple_list.index(word)] = word + "."
        print(" ".join(self.simple_list))


if __name__ == "__main__":
    programe = MakeSentence()
    programe.ask_for_sentence()
    programe.format_sentence()
