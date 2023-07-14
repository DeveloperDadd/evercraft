from character import Character
    
class Fighter(Character):
    def __init__(self):
        pass
    # Fighter // As a player I want to play a Fighter so that I can kick ass and take names
    #10 add health per level up instead of 5 
    #self.roll +=1

class Rogue(Character):
# Rogue // As a player I want to play a Rogue so that I can defeat my enemies with finesse
    def __init__(self): 
        self.alignment = "Evil"
        defender.dexterity.modifier = 0
        strength_modifier = dexterity_mod
        if self.roll == 20:
            damage = 3 

# Monk // As a player I want to play a Monk so that I can enjoy being an Asian martial-arts archetype in a Medieval European setting
class Monk(Character):
    def __init__(self):
        self.hitpoints_leveler = 6
        self.damage = 3    
    #    armor_class = wisdom.modifier only if it is greater than 0
    #    attack roll is increased by 1 every 2nd and 3rd level

# Paladin // As a player I want to play a Paladin so that I can smite evil, write wrongs, and be a self-righteous jerk
#The oath of throwing it back is great with us
class Paladin(Character):
    def __init__(self):
        super().__init__()  # Call the parent class's __init__ method
        self.hitpoints_leveler = 8
        self.alignment = 'Good'

    def check_damage(self, roll, defender):
        if defender.alignment == "Evil":
            self.damage += 2  # Add extra damage when attacking evil characters
        super().check_damage(roll, defender) 

    # Bard // As a player I want to play a Bard so that I can charm, inspire, seduce and entertain my allies/enemies alike
class Bard(Character):
    def __init__(self):
        self.hitpoints_leveler = 8

    #can cast one additional spell per level
    #can use Bardic Inspiration ability twice as many times per short rest

    # Cleric // As a player I want to play a Cleric so that I can heal the wounded, smite the undead, and serve my deity
class Cleric(Character):
    def __init__(self):
         self.hitpoints_leveler = 8

    #can cast two additional spells per level
    #double the number of hit points restored when using healing spells

# Druid // As a player I want to play a Druid so that I can shape-shift into animals, commune with nature, cast powerful spells and pretend I am a furry
class Druid(Character):
    def __init__(self):
        self.hitpoints_leveler = 8

    #can cast two additional spells per level
    #can use Wild Shape ability twice as many times per short rest
class Sorcerer(Character):
# Sorcerer // As a player I want to play a Sorcerer so that I can wield powerful arcane magic and unleash devastating spells
    def __init__(self):
        self.hitpoints_leveler = 6
        self.alignment = 'Neutral'

    #can cast two additional spells per level
    #spells deal +1 damage per die rolled



class Warlock(Character):
# Warlock // As a player I want to play a Warlock so that I can make a pact with a powerful entity and wield eldritch magic
    def __init__(self):
        self.hitpoints_leveler = 6

    #can cast two additional spells per level
    #gain +2 bonus to spell attack rolls and damage rolls
    #if defender.alignment == "Good":
    #    self.damage += 2

class Wizard(Character):
# Wizard // As a player I want to play a Wizard so that I can study ancient tomes, learn a wide variety of spells, and unravel arcane mysteries ( I die to literally anything
    def __init__(self):    
        self.hitpoints_leveler = 6
    #can cast two additional spells per level
    #can add +1 to spell save DC

class Ranger(Character):
# Ranger // As a player I want to play a Ranger so that I can be a skilled tracker, master of ranged combat, and have a bond with the wilderness
    def __init__(self):
        self.hitpoints_leveler = 8
    #gain +2 bonus to attack rolls and damage rolls with ranged weapons
    #can track creatures with advantage