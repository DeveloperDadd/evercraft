#Create a character as part of the assignment
from ArmorAndHP import Armor_And_Hitpoints
from CanAttack import CanAttack

class Character:
    def __init__(self):
        self.name = 'Cletus'

    #takes in a string
    def set_name(self, n):
        self.name = n
    
    def set_alignment(self, alignment):
        self.alignment = alignment




'''
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, target):
        damage = self.strength
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(self.name + " has been defeated!")

    def heal(self, amount):
        self.health += amount

    def display_status(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Strength:", self.strength)
'''

