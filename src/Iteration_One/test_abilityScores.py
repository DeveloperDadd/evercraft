from character import Character

def test_check_abilityscores():
    s = Character()
    assert s.strength == 10

    c = Character()
    assert c.strength_mod == 0

    t = Character()
    t.strength = 20
    t.set_modifiers()  # Call set_modifiers() to update the modifiers
    assert t.strength_mod == 5

# Run the test case
test_check_abilityscores()