import random


class Heroe(object):

    def __init__(self, name, total_health, current_health, armour_points, action_points, expirience=0):
        self.name = name
        self.total_health = total_health
        self.current_health= current_health
        self.armour = armour_points
        self.action_points = action_points
        self.expirience = expirience

    def level_up(self):
        if random.randint(0, 100) < 5:
            self.total_health += 10
            self.armour += 10
            self.action_points += 2
            self.expirience += 10
            print('You leveled up! Gained +10 to skills.')

    def healing(self):
        if self.current_health < self.total_health:
            healed_wounds = self.total_health - self.current_health
            if random.randint(0, 100) < 80:
                if (self.current_health + 20) > self.total_health:
                    self.current_health += healed_wounds
                else:
                    self.current_health + 20
            else:
                if (self.current_health + 10) > self.total_health:
                    self.current_health += healed_wounds
                else:
                    self.current_health + 10
        return self.current_health



class Attack(object):

    def __init__(self, basic_attack, strong_attack, knockdown=False):
        self.basic_attack = basic_attack
        self.strong_attack = strong_attack
        self.knockdown = self.strong_attack * 2.5

    def chance_of_hitting(self, executable):
        'function serving as a decorator'

        def wrapper(self):
            if random.randint(0, 100) < 80:
                executable()
            else:
                print('miss !')
                pass

        return wrapper

    def weak_melee(self, basic_attack):
        damage = random.randrange(basic_attack, basic_attack + 10)
        return damage

    def strong_melee(self, strong_attack):
        damage = random.randrange(strong_attack, strong_attack + 10)
        return damage

    def knockdown_attack(self, knockdown):
        if random.randint(0, 100) < 10:
            damage = self.knockdown
        return damage
