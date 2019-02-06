import random


class Deck(object):
    """Class representing playing cards.
        Cards have their own color and value.
        They can be stashed in a card deck, or hold in our hand
    """
    colors = ["Diamonds", "Spades", "Clubs", "Hearts"]
    value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.card_deck = []

    def deck_constructor(self):
        "Constructor of our deck"
        self.card_deck = [(value, color) for value in self.value for color in self.colors]
        return self.card_deck

    def deck_shuffle(self):
        "shuffles cards each time before play."
        return random.shuffle(self.card_deck)

    def draw(self):
        "function to draw a unic card from the deck, without returning it."
        draw = (random.choice(self.card_deck))
        self.card_deck.pop(self.card_deck.index(draw))
        return draw


class Hand(object):

    def __init__(self):
        self.hand = []

    def __str__(self):
        print(self.hand)

    def value_counter(self):
        value = 0
        for card in self.hand:
            if card[0] == 'Jack' or card[0] == "Queen" or card[0] == "King":
                value += 10
            elif type(card[0]) == int:
                value += card[0]
            else:
                if value < 11:
                    value += 11
                else:
                    value += 1
        return value

    def is_bust(self):
        if self.value_counter() > 21:
            print("YOU ARE BUST! Your hand score excited 21 and currently is {}".format(self.value_counter()))
            return True
        else:
            print("You are still in game, your current hand score is {}".format(self.value_counter()))
            return False


class Chips(object):

    def __init__(self):
        self.money = 100

    def make_bet(self):
        while True:
            anwser = int(input('How much do you wish to gamble?'))
            if anwser > 0 and anwser < self.money:
                self.money - anwser
                return anwser


if __name__ == "__main__":
    Card_Deck = Deck()
    Player_Hand = Hand()
    Dealers_Hand = Hand()
    Player_Chips = Chips()
    Dealers_Chips = Chips()
    Card_Deck.deck_constructor()
    Card_Deck.deck_shuffle()
    bankroll = 0
    game_on = True
    Player_Turn = True
    Dealers_Turn = True

while game_on:
    print('-' * 70)
    print("You have {} money in your pocket".format(Player_Chips.money))
    stake = Player_Chips.make_bet()
    bankroll = stake * 2
    Dealers_Chips.money - stake
    print("Current stake is '{}'$".format(bankroll))
    print('-'*70)
    for _ in range(0, 2):
        Card_Deck.draw()
        Player_Hand.hand.append(Card_Deck.draw())
    print('Your current hand is: {}'.format(Player_Hand.hand))
    for _ in range(0, 2):
        Card_Deck.draw()
        Dealers_Hand.hand.append(Card_Deck.draw())
    print('Dealers hand is: {}'.format(Dealers_Hand.hand[0]))
    Player_Hand.is_bust()
    while Player_Turn:
        question = input("Would you like to take a card ? Y/N")
        if question in ('y', 'Y'):
            Card_Deck.draw()
            Player_Hand.hand.append(Card_Deck.draw())
            Player_Hand.value_counter()
            print('Your current hand is: {}'.format(Player_Hand.hand))
            if Player_Hand.is_bust() == True:
                Player_Turn = False
                Dealers_Turn = False
                print('Sorry, try your luck next time')
                break
        else:
            print("It's Dealers turn to play!")
            break
    while Dealers_Turn:
        while Dealers_Hand.value_counter() <= 17:
            Card_Deck.draw()
            Dealers_Hand.hand.append(Card_Deck.draw())
            Dealers_Hand.value_counter()
            print('Dealers hand is: {}'.format(Dealers_Hand.hand))
            if Dealers_Hand.is_bust() == True:
                break
        break
    if Dealers_Hand.is_bust() == True:
        Player_Chips.money += bankroll
        print('-' * 70)
        print("You have won {} !".format(bankroll))
        print('\n' * 10)
    elif Player_Hand.value_counter() <= 21 and Player_Hand.value_counter() > Dealers_Hand.value_counter():
        Player_Chips.money += bankroll
        print('-'*70)
        print("YOU HAVE WON {} $!".format(bankroll))
        print("Your Hand card value is '{}' against delears Hand '{}' value".format(Player_Hand.value_counter(),
                                                                                    Dealers_Hand.value_counter()))
        print('\n'*5)
    else:
        print('-' * 70)
        print("YOU HAVE LOOSE")
        print("Your Hand card value is '{}' against delears Hand '{}' value".format(Player_Hand.value_counter(),
                                                                                    Dealers_Hand.value_counter()))
        print('-'*70)
        print('\n' * 5)
