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

    def add_modifiers(self, ):
        abmods = [0,0,0,0,0,0]
        abmods[0] = floor((strength - 10) / 2) #abilities = [0]
        abmods[1] = floor((dexterity - 10) / 2)#if dexterity is 10 then mod is 0 if 20 then +5
        abmods[2] = floor((constitution - 10) / 2)
        abmods[3] = floor((wisdom - 10) / 2)
        abmods[4] = floor((intelligence - 10) / 2)
        abmods[5] = floor((charisma - 10) / 2)


