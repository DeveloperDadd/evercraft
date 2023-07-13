from Character import Character

# TEST 1
# This test is designed to check if the xp of 'self' goes up by 10 after a successful hit (whether critical or normal) on the enemy and also that it keeps incrementing
def test_get_xp():
    self = Character()
    defender = Character()
    self.can_attack = True

    #Critical Hit
    Character.check_damage(self, 20, defender)
    assert self.current_xp == 10

    #Next consecutive hit
    Character.check_damage(self, 19, defender)
    assert self.current_xp == 20


