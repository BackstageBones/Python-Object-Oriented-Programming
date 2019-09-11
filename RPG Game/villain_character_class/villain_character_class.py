from character_abstractclass.character_abstractclass import CharacterAbstractClass
from class_exceptions.class_exception import MethodNotCallableForThatClass


class Villain(CharacterAbstractClass):
    default_health_points = 100

    def __init__(self, basic_damage, strong_damage):
        self.weak_attack = basic_damage
        self.strong_damage = strong_damage
        super().__init__(self.default_health_points)

    def healing(self):
        raise MethodNotCallableForThatClass

    def weak_attack(self):
        return self.weak_attack

    def strong_attack(self):
        return self.strong_attack

    def level_up(self):
        raise MethodNotCallableForThatClass

    def special_ability(self):
        pass

    @classmethod
    def override_health_points(cls, hp):
        cls.default_health_points = hp

    @classmethod
    def from_constants(cls, innit_constant):
        basic_damage, strong_damage = innit_constant
        return cls(basic_damage, strong_damage)
