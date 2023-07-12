from CanAttack import CanAttack
import random
#As a combatant I want to be able to attack other combatants so that I can survive to fight another day
#Roll a 20 sided die
#Roll must meet or beat opponents armor class to hit
#A roll of 20 always hits



def test_can_attack():
    # Simulate attacking with a roll of 10 and an opponent armor class of 12
    result = CanAttack(10, 12)
    
    # Assert that the result is False, as the roll of 10 is lower than the opponent's armor class
    assert result is False

    # Simulate attacking with a roll of 15 and an opponent armor class of 12
    result = CanAttack(15, 12)
    
    # Assert that the result is True, as the roll of 15 is equal to or higher than the opponent's armor class
    assert result is True

    # Simulate attacking with a roll of 20 (critical hit) and an opponent armor class of 10
    result = CanAttack(20, 10)
    
    # Assert that the result is True, as a roll of 20 always hits regardless of the opponent's armor class
    assert result is True