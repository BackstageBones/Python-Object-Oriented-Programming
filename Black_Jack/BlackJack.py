import random

class Deck(object):
    """Class representing playing cards.
        Cards have their own color and value.
        They can be stashed in a card deck, or hold on our hand
    """

    def __init__(self,colors,value,hand,card_deck):
        self.colors = colors
        self.value = value
        self.hand = hand
        self.card_deck = card_deck

    def deck_constructor(self):
        "Constructor of our deck"
        self.card_deck = [(value, color) for value in self.value for color in self.colors]

    def deck_shuffle(self):
        "shuffles cards each time before play."
        return random.shuffle(self.card_deck)

    def draw(self):
        """function to draw a new card from the deck
            and it a to our hand. """
        x = random.choice(self.card_deck)
        if x not in self.hand:
            self.hand +=[x]

    def value_counter(self):
        """ function that counts if we won or we were bust!
            If Ace is in our hand, then counter splits itself making list,
            showing two possibilites of playing our cards.
        """
        value=[0,0]
        for card in self.hand:
            if card[0] == 'Jack':
                value[0]+= 10
            elif card[0] == 'Queen':
                value[0]+=10
            elif card[0] == 'King':
                value[0]+=10
            elif card[0]== 'Ace':
                value[1]+=value[0]+11
                value[0]+=1
            else:
                value[0]+=card[0]

        return value




if __name__ == "__main__":
    My_Deck = Deck(["Diamonds","Spades","Clubs","Hearts"],[1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace'],hand=[],card_deck=())
    My_Deck.deck_constructor()
    My_Deck.deck_shuffle()
    value=My_Deck.value_counter()
    print(My_Deck.card_deck)
    My_Deck.draw()
    My_Deck.draw()
    print(My_Deck.hand)
    print(My_Deck.value_counter())
