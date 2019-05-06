import characters
import player_actions
import time

def alien_activity_scroll():
    print('A', end='')
    time.sleep(.25)
    print('l', end='')
    time.sleep(.25)
    print('i', end='')
    time.sleep(.25)
    print('e', end='')
    time.sleep(.25)
    print('n', end=' ')
    time.sleep(.25)
    print('A', end='')
    time.sleep(.25)
    print('c', end='')
    time.sleep(.25)
    print('t', end='')
    time.sleep(.25)
    print('i', end='')
    time.sleep(.25)
    print('v', end='')
    time.sleep(.25)
    print('i', end='')
    time.sleep(.25)
    print('t', end='')
    time.sleep(.25)
    print('y', end='')
    time.sleep(.25)
    print('.', end='')
    time.sleep(.25)
    print('.', end='')
    time.sleep(.25)
    print('.\n')
    time.sleep(.25)


def engagement(player1, player2, player3, player4, alien1, alien2, alien3):
    """ Initiate fight sequence between player and 3 aliens """

    enemy1 = characters.Sectoid(alien1)
    enemy2 = characters.Floater(alien2)
    enemy3 = characters.ThinMan(alien3)

    enemies = [enemy1, enemy2, enemy3]
    players = [player1, player2, player3, player4]

    print('Enemies appear:')
    for enemy in enemies:
        print(enemy.name)
    print()

    # while list 'enemies' is not empty
    while enemies:

        def individual_soldier_turn(player, enemies):

            if not enemies:
                return

            else:
                print(player.name, '\b:')
                print('1. Fire Weapon\n2. Reload')
                player_action = input('Select an action: ').lower()
                print()

                if player_action == '1' or player_action == 'fire weapon':
                    # fire at enemy 'target'
                    target_no = player.pick_target(enemies)
                    target = enemies[target_no]
                    player.fire_weapon(target)
                    if target.hp <= 0:
                        print(target.name, 'was killed!\n')
                        enemies.remove(target)

                elif player_action == '2' or player_action == 'reload':
                    player.reload()
                    print('Reloaded, Ammo:', player.weapon.ammo, '\n')


        def individual_alien_turn(enemy, players):

            if not players:
                return

            else:
                target = enemy.alien_pick_target(players)
                enemy.alien_fire_weapon(target)


        # player turn
        for player in players:
            individual_soldier_turn(player, enemies)

        if enemies:
            alien_activity_scroll()

        # alien turn
        for enemy in enemies:
            individual_alien_turn(enemy, players)
