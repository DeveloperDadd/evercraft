from Character import Character

# As an attacker I want to be able to damage my enemies so that they will die and I will live
# If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
# When hit points are 0 or fewer, the character (defender) is dead

def test_getRekt():
    x = Get_Rekt()
    defender = Character()
    defender.armor = 3
    defender.healthpoints = 5
   
    # when character is hit. loses of point of health, if its a 20 lose 2 points
    result = x.check_damage(20, defender)
    assert defender.healthpoints == 3

    result = x.check_damage(19, defender)
    assert defender.healthpoints == 2