import math
from character import Character


# Test 1
# Testing that the default level is level 1
def test_get_level():
    x = Character()
    assert x.level == 1

# Test 2 
# Testing that 1000xp comes out to equal level
def test_get_level1():
    x = Character()
    x.current_xp = 1000
    x.total_xp = 1000
    # how do we know that x.level is actually 2 or 1? when it says assert 1 == 2 in the test fail?
    result = x.set_level()
    assert result == 2

# Test 3
# Testing for level 3
def test_get_level2():
    x = Character()
    x.current_xp = 1000
    x.total_xp = 2000
    result = x.set_level()
    assert result == 3