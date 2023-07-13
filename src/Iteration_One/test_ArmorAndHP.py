from ArmorAndHP import Armor_And_Hitpoints


def test_get_armorAndHP():
    armor = 10
    hitpoints = 5
    x = Armor_And_Hitpoints(armor, hitpoints)

    assert x.armor == armor
    assert x.hitpoints == hitpoints