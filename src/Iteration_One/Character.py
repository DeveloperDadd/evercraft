#Create a character as part of the assignment

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
    
    #This function checks the condition if CanAttack is True of False
    #If true then self can hit the defender for one damage point
    #If the roll == 20 then hit the defender for two damage points
    #If CanAttack == False then nothing happens
    def check_damage(self, roll, defender):
        self.roll = roll
        if CanAttack == True and self.roll < 20:
            defender.healthpoints = defender.healthpoints - 1
        elif CanAttack == True and self.roll == 20:
            defender.healthpoints = defender.healthpoints - 2
        else:
            return
