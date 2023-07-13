from character import Character
# Feature : As a character I want to have an alignment so that I have something 
# to guide my actions
# Can choose between Good, Evil, and Neutral
# Can get and set an alignment

def test_get_alignment():
    a = Character()
    assert a.alignment == 'Good'

def test_set_alignment(): 
    x = Character()
    x.set_alignment('Evil')
    assert x.alignment == 'Evil'
