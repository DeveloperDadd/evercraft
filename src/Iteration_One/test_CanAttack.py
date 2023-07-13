from Character import Character

# TEST 1

def test_check_attack():
    # Create a defender with armor class 12
    self = Character()
    defender = Character()
    defender.armor = 12
    
    # Simulate attacking with a roll of 10
    # SHOULD RETURN FALSE
    result = Character.check_attack(self, 10, defender)
    assert result is False

# TEST 2

def test_check_attack1():
    # Create a defender with armor class 8
    self = Character()
    defender = Character()
    defender.armor = 8 

    #Simulate attacking with a roll of 10
    #SHOULD RETURN TRUE
    result = Character.check_attack(self, 10, defender)
    assert result is True 