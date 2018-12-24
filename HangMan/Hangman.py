import random

def random_word():
    lista = ['Międzykontynentalny', 'konstantynopolitańczycy',
             'rozentuzjazmowany', 'wyidealizowany', 'żniwiarkomłocarnia']
    choice = random.choice(lista)
    return choice

def word_lengh(choice):
    word = [letter for letter in range(0,len(choice))]
    print(word)
    return word

def get_input():
    guess = str(input('guess a letter'))
    return guess

def find_index(choice,guess):
    return guess in choice

def placing(word,choice,guess):
        place = choice.index(guess)
        return place

def unhiding(word,place,guess):
    word[place] = guess.upper()

print("Welcome to HangMan game")
game_on = True
Shot = 0
choice = random_word()
word = word_lengh(choice)
while game_on:
    while Shot<10:
        Shot+=1
        guess = get_input()
        if find_index(choice,guess) == True:
            place = placing(word,choice,guess)
            unhiding(word,place,guess)
            print(word)
            print('No of chances:',10-Shot)
        else:
            print("You missed !\n try again")
            print('No of chances:',10- Shot)
    else:
        print("You Hanged\n password was",choice)
    game_on=False



