import random
import items


class Character:
    """ Create base character """

    def __init__(self):
        pass



class XcomSoldier(Character):
    """ Create player characters """

    def __init__(self):
        pass

    def pick_target(self, enemies):
        """ Return index of selection in list 'enemies' """

        lst = list(enemies)
        enumerated_lst = enumerate(enemies, 1)

        def print_lst():
            for idx, enemy in enumerated_lst:
                print("{}. {} HP: {}".format(idx, enemy.name, enemy.hp))

        while True:
            print_lst()
            selection = int(input('Select target: '))
            print()
            if selection > len(lst) or selection < 1:
                print('Please select a valid target')
                continue
            else:
                return selection - 1

    def fire_weapon(self, defender):
        """ Fire character's weapon at 'defender' """

        if self.weapon.ammo > 0:
            # calculate damage value
            damage = random.randint(self.damage_min, self.damage_max)

            # calculate hit
            hit_chance = self.aim - defender.defs     # + aim modifiers?
            print(hit_chance)                         # get rid of print statements eventually
            hit_actual = random.randint(1, 100)
            print(hit_actual)

            # on success
            if hit_actual <= hit_chance:
                print('Hit! ', end='')
                defender.hp -= damage
                print(damage, 'damage')
                self.weapon.ammo -= 1
                print('Ammo:', self.weapon.ammo, '\n')

            # on failure
            else:
                print('Miss!')
                self.weapon.ammo -= 1
                print('Ammo:', self.weapon.ammo, '\n')
                return None

        else:
            print('No ammo!\n')

    def reload(self):
        self.weapon.ammo = self.weapon.full_ammo


class Assault(XcomSoldier):

    def __init__(self, name):
        self.name = name
        self.weapon = items.shotgun
        self.damage_min = self.weapon.damage_min
        self.damage_max = self.weapon.damage_max
        self.aim = 60
        self.defs = 0
        self.hp = 6


class Infantry(XcomSoldier):

    def __init__(self, name):
        self.name = name
        self.weapon = items.assault_rifle
        self.damage_min = self.weapon.damage_min
        self.damage_max = self.weapon.damage_max
        self.aim = 70
        self.defs = 0
        self.hp = 6


class Gunner(XcomSoldier):

    def __init__(self, name):
        self.name = name
        self.weapon = items.machine_gun
        self.damage_min = self.weapon.damage_min
        self.damage_max = self.weapon.damage_max
        self.aim = 65
        self.defs = 0
        self.hp = 6


class Sniper(XcomSoldier):

    def __init__(self, name):
        self.name = name
        self.weapon = items.sniper_rifle
        self.damage_min = self.weapon.damage_min
        self.damage_max = self.weapon.damage_max
        self.aim = 75
        self.defs = 0
        self.hp = 6



class AlienSoldier(Character):
    """ Create enemy characters """

    def __init__(self,):
        pass

    # pick a random xcom soldier
    def alien_pick_target(self, players):
        """ Picks player soldier """
        return random.choice(players)

    def alien_fire_weapon(self, defender):
        """ AI firing heuristic """

        print(self.name, 'fires at', defender.name, '\b!')
        damage = random.randint(self.damage_min, self.damage_max)

        hit_chance = self.aim - defender.defs
        hit_actual = random.randint(1, 100)

        if hit_actual <= hit_chance:
            print('Hit!', end=' ')
            defender.hp -= damage
            print(damage, 'damage')
            print(defender.name, 'Hp: ', defender.hp)
            print()
        else:
            print('Miss!\n')

class Sectoid(AlienSoldier):

    def __init__(self, name):
        self.name = name
        self.damage_min = 1
        self.damage_max = 2
        self.aim = 55
        self.defs = 0
        self.hp = 3


class Floater(AlienSoldier):

    def __init__(self, name):
        self.name = name
        self.damage_min = 2
        self.damage_max = 3
        self.aim = 60
        self.defs = 0
        self.hp = 4


class ThinMan(AlienSoldier):

    def __init__(self, name):
        self.name = name
        self.damage_min = 3
        self.damage_max = 4
        self.aim = 70
        self.defs = 0
        self.hp = 5
