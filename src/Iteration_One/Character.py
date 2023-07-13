#Create a character as part of the assignment
from ArmorAndHP import Armor_And_Hitpoints
from CanAttack import CanAttack

class Character:
    def __init__(self, armor = 10.0, hitpoints = 5.0):
        self.name = 'Cletus'
        self.armor = armor
        self.hitpoints = hitpoints

    #takes in a string 
    def set_name(self, n):
        self.name = n
    
    def set_alignment(self, alignment):
        self.alignment = alignment

    #This function checks if a dice roll is higher than the defender's armor class
    #If it is then the character can hit the defender
    def check_attack(self, roll, defender):
        self.roll = roll
        canAttack = False
        if self.roll > defender.armor:
            canAttack = True
        else:
            canAttack = False
        return canAttack
    

