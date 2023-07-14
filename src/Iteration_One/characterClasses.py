from character import Character

class OrcShaman(Character):
    def __init__(self):
        self.name = 'Drakka Bloodhowl'
    
class Fighter(Character):
    # Fighter // As a player I want to play a Fighter so that I can kick ass and take names
    #10 add health per level up instead of 5 
    self.roll +=1

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
        self.hitpoints_leveler = 8
        self.alignment = 'Good'

    #+2 to attack and damage when attacking Evil characters 
    if defender.alignment =="Evil":
        
does triple damage when critting on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
attacks roll is increased by 1 for every level instead of every other level

# Bard // As a player I want to play a Bard so that I can charm, inspire, seduce and entertain my allies/enemies alike
class Bard(Character):
    def __init__(self):
        self.hitpoints_leveler = 8

can cast one additional spell per level
can use Bardic Inspiration ability twice as many times per short rest

# Cleric // As a player I want to play a Cleric so that I can heal the wounded, smite the undead, and serve my deity
class Cleric(Character):
    def __init__(self):
        self.hitpoints_leveler = 8

can cast two additional spells per level
double the number of hit points restored when using healing spells

# Druid // As a player I want to play a Druid so that I can shape-shift into animals, commune with nature, cast powerful spells and pretend I am a furry
class Druid(Character)
    def __init__(self):
        self.hitpoints_leveler = 8

can cast two additional spells per level
can use Wild Shape ability twice as many times per short rest

# Sorcerer // As a player I want to play a Sorcerer so that I can wield powerful arcane magic and unleash devastating spells
class Sorcerer(Character):
    def __init__(self):
        self.hitpoints_leveler = 6
        self.alignment = 'Neutral'

can cast two additional spells per level
spells deal +1 damage per die rolled


# Warlock // As a player I want to play a Warlock so that I can make a pact with a powerful entity and wield eldritch magic
class Warlock(Character):
    def __init__(self):
        self.hitpoints_leveler = 6

can cast two additional spells per level
gain +2 bonus to spell attack rolls and damage rolls
+2 damage to Good characters

# Wizard // As a player I want to play a Wizard so that I can study ancient tomes, learn a wide variety of spells, and unravel arcane mysteries ( I die to literally anything
class Wizard(Character)

6 add health per level up instead of 5
can cast two additional spells per level
can add +1 to spell save DC

# Ranger // As a player I want to play a Ranger so that I can be a skilled tracker, master of ranged combat, and have a bond with the wilderness
8 add health per level up instead of 5
gain +2 bonus to attack rolls and damage rolls with ranged weapons
can track creatures with advantage

