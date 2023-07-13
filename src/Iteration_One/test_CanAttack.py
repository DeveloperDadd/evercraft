from Character import Character

def test_can_attack():
    # Create a defender with armor class 12
    defender = Character()
    defender.armor = 12

    # Create an instance of CanAttack
    attack = Character.check_attack

    # Simulate attacking with a roll of 10
    result = attack(10, defender)
    assert result is False
