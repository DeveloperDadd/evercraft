from Character import Character

# As an attacker I want to be able to damage my enemies so that they will die and I will live
# If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
# When hit points are 0 or fewer, the character (defender) is dead

#TEST 1

def test_check_damage():
    self = Character()
    defender = Character()
    self.can_attack = True
   
    #When roll == 20 subtract two from defender healthpoints
    result = Character.check_damage(self, 20, defender)
    assert defender.hitpoints == 3

    #When roll > 20 and CanAttack = True, subtract 1 hitpoint
    result = Character.check_damage(self, 19, defender)
    assert defender.hitpoints == 2

# TEST 2
# This test is designed to see if the enemy hitpoints drops to zero
    
def test_check_damage1():
    self = Character()
    defender = Character()
    defender.hitpoints = 1
    self.can_attack = True

    # Test critical hit
    result = Character.check_damage(self, 20, defender)
    assert defender.hitpoints <= 0

   

# TEST 3
# Test normal hit
def test_check_damage2():
    self = Character()
    defender = Character()
    defender.hitpoints = 1
    self.can_attack = True

    result = Character.check_damage(self, 19, defender)
    assert defender.hitpoints == 0

