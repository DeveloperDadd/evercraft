from characterClasses import Paladin

def test_paladin_damage():
    p = Paladin()
    defender = Character()
    defender.alignment = 'Evil'
    p.can_attack = True
    defender.hitpoints = 10

    p.check_damage(self, 19, defender)
    assert defender.hitpoints == 8
