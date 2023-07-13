from Character import Character
# As a character I want to have several abilities so that I am not identical to other
# characters except in name
# Abilities are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
# Abilities range from 1 - 20 and default to 10

class Abilities():
    def __init__(self, strength = 10, dexterity = 10, constitution = 10, 
    wisdom = 10, intelligence = 10, charisma = 10):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    #def add_modifier():
        
