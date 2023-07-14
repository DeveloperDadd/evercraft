#Create a character as part of the assignment
import math

class Character:
    def __init__(self, armor = 10.0, hitpoints = 5.0, can_attack = False, damage=1,
     current_xp = 0, total_xp = 0, level = 1, strength = 10, dexterity = 10, constitution = 10, 
    wisdom = 10, intelligence = 10, charisma = 10):
    
        #Character Info
        self.name = 'Leopold Ironfist'
        self.alignment = 'Neutral'
        self.armor = armor #Armor class = 10
        self.hitpoints = hitpoints #Hitpoints = 5

        #CAN ATTACK & DAMAGE VALUES
        self.can_attack = can_attack #Default set to False
        self.damage = damage #Default damage = 1

        #LEVELS
        self.current_xp = current_xp
        self.total_xp = total_xp
        self.level = level #Default level is 1

        #ABILITIES all DEFAULT to a Score of 10
        self.strength = strength 
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
    
        self.set_modifiers()
    #Abilities Modifiers
    def set_modifiers(self):
        self.strength_mod = math.floor((self.strength - 10) / 2)
        self.dexterity_mod = math.floor((self.dexterity - 10) / 2)
        self.constitution_mod = math.floor((self.constitution - 10) / 2)
        self.wisdom_mod = math.floor((self.wisdom - 10) / 2)
        self.intelligence_mod = math.floor((self.intelligence - 10) / 2)
        self.charisma_mod = math.floor((self.charisma - 10) / 2)
    
    #Set total ability 
    #def set_total_ability(self):

    
    #takes in a string 
    def set_name(self, n):
        self.name = n
    
    def set_alignment(self, alignment):
        self.alignment = alignment

    #This function checks if a dice roll is higher than the defender's armor class
    #If it is then the character can hit the defender
    def check_attack(self, roll, defender):
        self.roll = roll
        if self.roll > defender.armor:
            can_attack = True
        else:
            can_attack = False
        return can_attack
    
    #This function checks the condition if CanAttack is True of False
    #If true then self can hit the defender for one damage point
    #If the roll == 20 then hit the defender for two damage points
    #If CanAttack == False then nothing happens
    def check_damage(self, roll, defender):
        self.roll = roll
        if self.can_attack == True and self.roll < 20:
            defender.hitpoints = defender.hitpoints - self.damage
            self.current_xp += 10
            self.total_xp += 10
            if defender.hitpoints == 0:
                print('You have slain your enemy!')
        elif self.can_attack == True and self.roll == 20:
            defender.hitpoints = defender.hitpoints - self.damage * 2
            self.current_xp += 10
            self.total_xp += 10
            if defender.hitpoints <= 0:
                print('You decapitate your enemy and put his head on a pike. Hoorah!')
        else:
            return
        return defender.hitpoints
    

    # As a character I want my experience points to increase my level and combat capabilities
    # So that I can bring vengeance to my foes
    # Every 1000 xp points, the character levels up
    # For each level hitpoints goes up by 5
    # 1 damage is added to the attack roll 
    def set_level(self):
        xp_limit = 1000
        if self.current_xp >= xp_limit: 
            self.level = (math.floor(self.total_xp / 1000) + 1)
            self.hitpoints = self.hitpoints + 5
            self.damage = self.damage + 1
            print("Unleash your newfound power. All who oppose you shall suffer")
            self.current_xp = self.current_xp - 1000
            xp_limit = self.level * 1000
            return self.level
        
