#STEP 1

from abc import ABC, abstractmethod

class IAttackStrategy(ABC):
    @abstractmethod
    def attack(self):
        pass


class SwordAttack(IAttackStrategy):
    def attack(self):
        return "Swings sword!"


class MagicMissileAttack(IAttackStrategy):
    def attack(self):
        return "Casts magic missile!"


class ArrowShotAttack(IAttackStrategy):
    def attack(self):
        return "Shoots an arrow!"


#STEP 2
class Character(ABC):
    def __init__(self, attack_strategy: IAttackStrategy):
        self.attack_strategy = attack_strategy
        self.health = 100

    def attack(self):
        return self.attack_strategy.attack()


#STEP 3
class Warrior(Character):
    def __init__(self):
        super().__init__(SwordAttack())


class Mage(Character):
    def __init__(self):
        super().__init__(MagicMissileAttack())


class Archer(Character):
    def __init__(self):
        super().__init__(ArrowShotAttack())


#STEP 4
class CharacterFactory:
    @staticmethod
    def create_character(character_type: str) -> Character:
        if character_type == "warrior":
            return Warrior()
        elif character_type == "mage":
            return Mage()
        elif character_type == "archer":
            return Archer()
        else:
            raise ValueError("Unknown character type")