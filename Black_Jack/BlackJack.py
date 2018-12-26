import random

class Deck(object):

    def __init__(self,colors,value,hand,card):
        self.colors = colors
        self.value = value
        self.hand = hand
        self.card = card

    def deck_constructor(self):
        self.card = [(value, color) for value in self.value for color in self.colors]

    def deck_shuffle(self):
        return random.shuffle(self.card)

    def draw(self):
        self.hand += random.choice(self.card)

if __name__ == "__main__":
    My_Deck = Deck(["Diamonds","Spades","Clubs","Hearts"],[1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace'],hand=[],card=())
    My_Deck.deck_constructor()
    My_Deck.deck_shuffle()
    print(My_Deck.card)
    My_Deck.draw()
    print(My_Deck.hand)
