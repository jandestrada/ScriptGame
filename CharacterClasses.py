from EquipmentClasses import *

class Character():
    health = None #how much damage chr can take before dying
    strength = None #divide by attack coeff_ and add equipment to calculate dmg point
    intelligence = None #used to determine likelihood of damaging
    speed = None #used to determine likelihood of evading

    weapon = None #boosts damage
    chest_armor=None #protects against physical hits
    leg_armor = None #protects against stats hits

    label = None #used for printing what type of character you are

    name = None

class Traditional(Character):
    weapons_list = [SmallSword(),SmallAxe(),SmallKnife()]
    chest_armor_list = [CopperPlate(), WoolShirt(),LeatherPlate()]
    leg_armor_list = [CopperBrace(),WoolBrace(),LeatherBrace()]

class Bizarre(Character):
    weapons_list = None
    chest_armor_list = None
    leg_armor_list = None

class Human(Traditional):
    def __init__(self):
        self.health = 10 #units
        self.strength = 7 #units
        self.intelligence = 5 #units
        self.speed = 7 #units

        self.label = "HUMAN"




class Orc(Traditional):
    def __init__(self):
        self.health = 12
        self.strength = 11
        self.intelligence = 3
        self.speed = 4

        self.label = "ORC"

class Elf(Traditional):
    def __init__(self):
        self.health = 7
        self.strength = 5
        self.intelligence = 7
        self.speed = 12

        self.label = "ELF"

class MosqMan(Bizarre):
    def __init__(self):
        self.health = 4
        self.strength = 3
        self.intelligence = 4
        self.speed = 20

        self.weapons_list = [BloodStick(),ShrpBrknWing(), HardEggs()]
        self.chest_armor_list = [ChitinSkin(),HumanTissue(),DndrfFlakes()]
        self.leg_armor_list = [ChitinString(),HumanHair(),CatHair()]

        self.label= "MOSQUITO MAN"

class MrClean(Bizarre):
    def __init__(self):
        self.health = 7
        self.strength = 13
        self.intelligence = 15
        self.speed = 2

        self.weapons_list=[Sponge(),Plunger(),Mop()]
        self.chest_armor_list = [CrustySponge(),DirtyRag(),BblShirt()]
        self.leg_armor_list = [SpongeShoes(),SoapShoes(),BblShoes()]

        self.label = "MR. CLEAN HUMANOID"


class TPFeeders(Bizarre):
    def __init__(self):
        self.health = 16
        self.strength = 5
        self.intelligence = 1
        self.speed = 5

        self.weapons_list = [TastySoap(),NoTearShampoo(),ToiletSeat()]
        self.chest_armor_list = [TideBox(),PltcWrap(),ShameShirt()]
        self.leg_armor_list = [IdtJeans(),SoapPants(),BblShorts()]

        self.label = "TIDE POD FEEDER"




