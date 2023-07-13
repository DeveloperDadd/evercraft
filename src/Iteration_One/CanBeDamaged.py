
from ArmorAndHP import Armor_And_Hitpoints

class Get_Rekt:
    def __init__(self):
        pass

    def check_damage(self, roll, defender):
        self.roll = roll
        GetRekt = False
        if self.roll > defender.armor:
            GetRekt = True
            if self.roll == 20:
                defender.healthpoints = defender.healthpoints - 2
            elif self.roll < 20 and roll > defender.armor:
                defender.healthpoints = defender.healthpoints - 1  
        else:
            GetRekt = False
        return GetRekt