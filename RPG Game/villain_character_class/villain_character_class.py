from ..character_abstractclass import character_abstractclass
from class_exceptions.class_exception import MethodNotCallableForThatClass


class Villain(character_abstractclass):

    def __init__(self, name):
        self.name = name
        super(Villain, self).__init__()

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