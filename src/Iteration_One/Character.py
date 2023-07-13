#Create a character as part of the assignment

class Character:
    def __init__(self, armor = 10.0, hitpoints = 5.0, can_attack = False):
        self.name = 'Cletus'
        self.alignment = 'Good'
        self.armor = armor
        self.hitpoints = hitpoints
        self.can_attack = can_attack
        

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
            defender.hitpoints = defender.hitpoints - 1
            if defender.hitpoints == 0:
                print('You have slain your enemy!')
        elif self.can_attack == True and self.roll == 20:
            defender.hitpoints = defender.hitpoints - 2
            if defender.hitpoints <= 0:
                print('You decapitate your enemy and put his head on a pike. Hoorah!')
        else:
            return
        return defender.hitpoints
