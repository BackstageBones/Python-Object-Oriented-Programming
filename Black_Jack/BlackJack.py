import random

class Deck(object):

    def __init__(self,colors,value):
        self.colors = colors
        self.value = value

    def deck_constructor(self):
        card = [(value, color) for value in self.value for color in self.colors]
        return  card

if __name__ == "__main__":
    My_Deck = Deck(["Diamonds","Spades","Club","Hearts"],range(1,14))
    print(My_Deck.deck_constructor())