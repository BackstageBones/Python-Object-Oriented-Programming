import random

class Deck(object):
    """Class representing playing cards.
        Cards have their own color and value.
        They can be stashed in a card deck, or hold in our hand
    """
    colors = ["Diamonds","Spades","Clubs","Hearts"]
    value = [1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

    def __init__(self,card_deck):
        self.hand = []
        self.card_deck = card_deck


    def deck_constructor(self):
        "Constructor of our deck"
        self.card_deck = [(value, color) for value in self.value for color in self.colors]
        return  self.card_deck

    def deck_shuffle(self):
        "shuffles cards each time before play."
        return random.shuffle(self.card_deck)

    def draw(self):
        "function to draw a unic card from the deck, without returning it."
        x = (random.choice(self.card_deck))
        self.hand.append(x)
        self.card_deck.pop(self.card_deck.index(x))


    def value_counter(self):
        """ function that counts if we won or we were bust!
            If Ace is in our hand, then counter splits itself making list,
            showing two possibilites of playing our cards.
        """
        value = 0
        for card in self.hand:
            if card[0] == 'Jack' or card[0] == "Queen" or card[0] =="King" :
                value+=10
            elif type(card[0])==int:
                value+=card[0]
            else:
                if value <11:
                    value+=11
                else:
                    value+=1
        if value <=21:
            print("You are still in game, your current hand score is {}".format(value))
            return value
        else:
            print("You are BUST! Your hand score excited 21 and currently is {}".format(value))
        return value


bankroll = 0
class Player(object):

    def __init__(self):
        self.money = 100

    def make_bet(self):
        while True:
            anwser = int(input('How much do you wish to gamble?'))
            if anwser > 0 and anwser< self.money:


if __name__ == "__main__":
    My_Deck = Deck(card_deck=())
   
    My_Deck.deck_constructor()
    My_Deck.deck_shuffle()
    value=My_Deck.value_counter()
    print(My_Deck.card_deck)
    My_Deck.draw()
    My_Deck.draw()
    print(My_Deck.hand)
    (My_Deck.value_counter())

