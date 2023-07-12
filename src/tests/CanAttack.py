import random 
class CanAttack:
    def __init__(self):
        self.roll = random.randint(1, 20)

    def check_attack(self, armor_class, bonus_armor):
        effective_armor_class = armor_class + bonus_armor
        return self.roll >= effective_armor_class