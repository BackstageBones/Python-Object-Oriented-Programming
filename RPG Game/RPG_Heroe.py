import random

class Heroe(object):

    def __init__(self, name, health, armour_points, action_points, expirience):
        self.name = name
        self.health = health
        self.armour = armour_points
        self.action_points= action_points
        self.expirience = expirience

class Attack(object):

    def __init__(self, basic_attack, strong_attack, knockdown=False):
        self.basic_attack = basic_attack
        self.strong_attack = strong_attack
        self.knockdown = knockdown

    def weak_melee(self, basic_attack):
         damage =random.randrange(basic_attack, basic_attack+10)
         return damage

    def strong_melee(self, strong_attack):
        damage = random.randrange(strong_attack, strong_attack+10)
        return damage

    def knockdown_attack(self, knockdown):
        if self.knockdown == True:
            chance = random.randrange(20)
            if chance == 7:
                @strong_melee
            else:
                pass
        else:
            pass