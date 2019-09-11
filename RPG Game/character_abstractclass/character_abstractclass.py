from abc import ABC, abstractmethod


class CharacterAbstractClass(ABC):
    default_health_points = 100

    def __init__(self, health, weak_attack, strong_attack, experience_points):
        self.health = health
        self.weak_attack = weak_attack
        self.strong_attack = strong_attack
        self.experience_points = experience_points

    @abstractmethod
    def healing(self):
        pass

    @abstractmethod
    def weak_attack(self):
        pass

    @abstractmethod
    def strong_attack(self):
        pass

    @abstractmethod
    def level_up(self):
        pass

    @abstractmethod
    def special_ability(self):
        pass

    @classmethod
    def override_health_points(cls, hp):
        cls.default_health_points = hp
