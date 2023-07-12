from CanAttack import CanAttack
from Character import Character

def test_can_attack():
    # Create a defender with armor class 12
    defender = Character()
    defender.armor = 12

    # Create an instance of CanAttack
    attack = CanAttack()

    # Simulate attacking with a roll of 10
    result = attack.check_attack(10, defender)
    assert result is False

    # Simulate attacking with a roll of 15
    result = attack.check_attack(15, defender)
    assert result is True

    # Simulate attacking with a roll of 20 (critical hit)
    result = attack.check_attack(20, defender)
    assert result is True