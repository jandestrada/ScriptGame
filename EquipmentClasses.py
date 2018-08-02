class Equipment():
    hlt_boost = None
    str_boost = None
    int_boost = None
    spd_boost = None

    label = None
    description = None

## WEAPONS ##
class Weapon(Equipment):
    def __init__(self):
        self.hlt_boost = None
        self.str_boost = None
        self.int_boost = None
        self.spd_boost = None

        label = None
class SmallSword(Weapon):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 2
        self.int_boots = 0
        self.spd_boost = 1

        self.label = "SMALL SWORD"

class SmallAxe(Weapon):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 3
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "SMALL AXE"
class SmallKnife(Weapon):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 1
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "SMALL KNIFE"

class BloodStick(Weapon):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 1
        self.int_boost = 0
        self.spd_boost = 1

        self.label = "BLOOD STICK"
class ShrpBrknWing(Weapon):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 1
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "SHARP BROKEN WING"

class HardEggs(Weapon):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 2
        self.int_boost = 1
        self.spd_boost = 0

        self.label = "HARD EGGS"

class Sponge(Weapon):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 1
        self.spd_boost = 1

        self.label="SPONGE"

class Plunger(Weapon):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 2
        self.int_boost = 1
        self.spd_boost = 0

        self.label = "PLUNGER"

class Mop(Weapon):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 2
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "MOP"
class TastySoap(Weapon):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "TASTY SOAP"

class NoTearShampoo(Weapon):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 1
        self.spd_boost = 1

        self.label = "NO TEAR SHAMPOO"

class ToiletSeat(Weapon):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 2
        self.int_boost = 1
        self.spd_boost = 0

        self.label = "TOILET SEAT"

## ARMOR ##
class Armor(Equipment):
    def __init__(self):
        self.hlt_boost = None
        self.str_boost = None
        self.int_boost = None
        self.spd_boost = None

class CopperPlate(Armor):
    def __init__(self):
        self.hlt_boost = 3
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "COPPER PLATE"

class WoolShirt(Armor):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "WOOL SHIRT"

class LeatherPlate(Armor):
    def __init__(self):
        self.hlt_boost = 2
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 1

        self.label = "LEATHER PLATE"


class CopperBrace(Armor):
    def __init__(self):
        self.hlt_boost = 3
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "COPPER BRACE"


class WoolBrace(Armor):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "WOOL BRACE"


class LeatherBrace(Armor):
    def __init__(self):
        self.hlt_boost = 2
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 1

        self.label = "LEATHER BRACE"

class ChitinSkin(Armor):
    def __init__(self):
        self.hlt_boost = 3
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "CHITIN SKIN"

class HumanTissue(Armor):
    def __init__(self):
        self.hlt_boost = 2
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 1

        self.label = "HUMAN TISSUE"

class DndrfFlakes(Armor):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "DANDRUFF FLAKES"

class ChitinString(Armor):
    def __init__(self):
        self.hlt_boost = 3
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "CHITIN STRING"

class HumanHair(Armor):
    def __init__(self):
        self.hlt_boost = 2
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 1

        self.label = "HUMAN HAIR"

class CatHair(Armor):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "CAT HAIR"

class CrustySponge(Armor):
    def __init__(self):
        self.hlt_boost = 3
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "CRUSTY SPONGE"


class DirtyRag(Armor):
    def __init__(self):
        self.hlt_boost = 2
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 1

        self.label = "DIRTY RAG"


class BblShirt(Armor):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "BUBBLE SHIRT"


class SpongeShoes(Armor):
    def __init__(self):
        self.hlt_boost = 3
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "OLD-SPONGE SHOES"


class SoapShoes(Armor):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "SOAP SHOES"


class BblShoes(Armor):
    def __init__(self):
        self.hlt_boost = 0
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 3

        self.label = "BUBBLE SHOES"


class TideBox(Armor):
    def __init__(self):
        self.hlt_boost = 3
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "TIDE BOX"


class PltcWrap(Armor):
    def __init__(self):
        self.hlt_boost = 2
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 1

        self.label = "PLASTIC WRAP"


class ShameShirt(Armor):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "SHAME SHIRT"

class IdtJeans(Armor):
    def __init__(self):
        self.hlt_boost = 3
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 0

        self.label = "IDIOT JEANS"


class SoapPants(Armor):
    def __init__(self):
        self.hlt_boost = 2
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 1

        self.label = "SOAP PANTS"


class BblShorts(Armor):
    def __init__(self):
        self.hlt_boost = 1
        self.str_boost = 0
        self.int_boost = 0
        self.spd_boost = 2

        self.label = "BUBBLE SHORTS"



