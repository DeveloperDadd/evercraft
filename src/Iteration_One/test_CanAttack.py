from Character import Character

def test_can_attack():
    # Create a defender with armor class 12
    defender = Character()
    defender.armor = 12

    # Simulate attacking with a roll of 10
    result = Character.check_attack(10, defender)
    assert result is False
