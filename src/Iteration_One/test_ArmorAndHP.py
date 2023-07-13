from Character import Character

def test_get_armorAndHP():
    x = Character()

    assert x.armor == 10
    assert x.hitpoints == 5