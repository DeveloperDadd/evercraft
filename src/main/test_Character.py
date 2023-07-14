from character import Character
# Feature : Create a Character
# As a character I want to have a name so that I can be distinguished from other characters
# Can get a set Name

def test_get_name():
    c = Character()
    assert c.name == 'Leopold Ironfist'

def test_set_name():
    d = Character()
    d.set_name('Joe')
    assert d.name == 'Joe'

def test_set_name2():
    d = Character()
    d.set_name('Joe')
    assert d.name == 'Joe'

def test_get_alignment():
    d = Character()
    assert d.alignment == 'Neutral'