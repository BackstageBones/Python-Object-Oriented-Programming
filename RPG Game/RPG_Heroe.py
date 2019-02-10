import random

class Heroe(object):

    def __init__(self, name, health, armour_points, action_points, expirience=0):
        self.name = name
        self.health = health
        self.armour = armour_points
        self.action_points= action_points
        self.expirience = expirience


    def level_up(self):
        if random.randint(0, 100) < 5:
            self.health += 10
            self.armour += 10
            self.action_points += 2
            self.expirience += 10
            print('You leveled up! Gained +10 to skills.')

class Attack(object):

    def __init__(self, basic_attack, strong_attack, knockdown=False):
        self.basic_attack = basic_attack
        self.strong_attack = strong_attack
        self.knockdown = self.strong_attack *2.5

    def chance_of_hitting(self,executable):
        'function serving as a decorator'
        if random.randint(0, 100) < 80:
            executable()
        else:
            print('miss !')


    def weak_melee(self, basic_attack):
         damage =random.randrange(basic_attack, basic_attack+10)
         return damage

    def strong_melee(self, strong_attack):
        damage = random.randrange(strong_attack, strong_attack+10)
        return damage

    def knockdown_attack(self, knockdown):
        if random.randint(0, 100) < 10:
            damage = self.knockdown
            return damage