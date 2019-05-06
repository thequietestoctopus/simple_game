class Item:

    def __init__(self):
        pass


class Weapon(Item):

    def __init__(self):
        pass


class AssaultRifle(Weapon):

    def __init__(self):
        self.full_ammo = 3
        self.ammo = 3
        self.damage_min = 3
        self.damage_max = 5
        self.range = 12


class Shotgun(Weapon):

    def __init__(self):
        self.full_ammo = 3
        self.ammo = 3
        self.damage_min = 3
        self.damage_max = 5
        self.range = 6


class MachineGun(Weapon):

    def __init__(self):
        self.full_ammo = 5
        self.ammo = 5
        self.damage_min = 4
        self.damage_max = 6
        self.range = 12


class SniperRifle(Weapon):

    def __init__(self):
        self.full_ammo = 3
        self.ammo = 3
        self.damage_min = 3
        self.damage_max = 5
        self.range = 18



# instantiate classes

assault_rifle = AssaultRifle()
shotgun = Shotgun()
machine_gun = MachineGun()
sniper_rifle = SniperRifle()
