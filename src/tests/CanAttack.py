import random 

class CanAttack:
    def __init__(self):
        pass

    def check_attack(self, roll, defender):
        self.roll = roll
        canAttack = False
        if self.roll > defender.armor:
            canAttack = True
        else:
            canAttack = False
        return canAttack