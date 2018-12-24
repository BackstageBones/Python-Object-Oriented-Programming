import random

class Deck(object):

    colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def deck_constructor(self,):
        deck = []
        for i in range(1, 14):
            for color in self.colors:
                deck.append({"color)": i})
        return deck

if __name__ == "__main__":
    My_Deck = Deck()
    My_Deck.deck_constructor()