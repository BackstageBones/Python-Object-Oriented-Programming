from abc import ABC, abstractmethod


class CharacterAbstractClass(ABC):

    def __init__(self, health):
        self.health = health

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
