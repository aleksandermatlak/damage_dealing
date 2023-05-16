import random
import math

class Enemy:
    def __init__(self, name: str, hp: int, armor: int):
        self.name = name
        self.hp = hp
        self.armor = armor


def create_enemies():
    number = random.randint(1, 9)
    enemies = []
    for i in range(number):
        enemies.append(Enemy(f'Przeciwnik {i + 1}', random.randint(1, 100), random.randint(1, 100)))
    return enemies


class Weapon:
    def __init__(self, name: str, weapon_type: str):
        self.name = name
        self.weapon_type = weapon_type


def deal_dmg(weapon: Weapon, enemy: list, en_number: int):
    print(f'Wybrano broń {weapon.name}, typu: {weapon.weapon_type}.')
    damage = abs(math.ceil(random.normalvariate(100, 50)))
    if weapon.weapon_type == 'Hitscan':
        enemy[en_number - 1].hp = enemy[en_number - 1].hp - math.ceil((damage * (1 - (enemy[en_number - 1].armor / 100) / 2)))
        print(f'{enemy[en_number - 1].name} otrzymał {math.ceil((damage * (1 - (enemy[en_number - 1].armor / 100) / 2)))} obrażeń.' + '\n')
        if enemy[en_number - 1].hp <= 0:
            print(f'{enemy[en_number - 1].name} umarł.' + '\n')
    if weapon.weapon_type == 'Projectile':
        hit_chance = random.randint(0, 1)
        if hit_chance:
            damage = abs(math.ceil(random.normalvariate(100, 50)))
            enemy[en_number - 1].hp = \
                enemy[en_number - 1].hp - math.ceil(damage * (1 - (enemy[en_number - 1].armor / 100 / 2)))
            print(f'{enemy[en_number - 1].name} otrzymał {math.ceil(damage * (1 - (enemy[en_number - 1].armor / 100 / 2)))} obrażeń.' + '\n')
            if enemy[en_number - 1].hp <= 0:
                print(f'{enemy[en_number - 1].name} umarł.' + '\n')
        else:
            print('Strzał nietrafiony.' + '\n')
    if weapon.weapon_type == 'Area':
        hit_chance = random.randint(0, 1)
        if hit_chance:
            enemy[en_number - 1].hp = enemy[en_number - 1].hp - math.ceil(damage * (1 - (enemy[en_number - 1].armor / 100 / 2)))
            print(f'{enemy[en_number - 1].name} otrzymał {math.ceil(damage * (1 - (enemy[en_number - 1].armor / 100 / 2)))} '
                  f'obrażeń.' + '\n')
            if enemy[en_number - 1].hp <= 0:
                print(f'{enemy[en_number - 1].name} umarł.' + '\n')
            modifier = 0.75
            for i in range(en_number - 2, -1, -1):
                dmg = math.ceil(((damage * (1 - (enemy[i].armor / 100 / 2))) * modifier))
                enemy[i].hp = enemy[i].hp - dmg
                modifier -= 0.25
                print(f'{enemy[i].name} '
                      f'otrzymał {dmg} obrażeń.' + '\n')
                if enemy[i].hp <= 0:
                    print(f'{enemy[i].name} umarł.' + '\n')
                else:
                    continue
            modifier = 0.75
            for i in range(en_number, len(enemy)):
                if modifier > 0:
                    dmg = math.ceil(((damage * (1 - (enemy[i].armor / 100 / 2))) * modifier))
                    enemy[i].hp = enemy[i].hp - dmg
                    modifier -= 0.25
                    print(f'{enemy[i].name} '
                          f'otrzymał {dmg} obrażeń.' + '\n')
                    if enemy[i].hp <= 0:
                        print(f'{enemy[i].name} umarł.' + '\n')
                else:
                    continue
        else:
            print('Strzał nietrafiony.' + '\n')
    dead_enemies = []
    for i in range(len(enemy)):
        if enemy[i].hp <= 0:
            dead_enemies.append(enemy[i])
    for dead_enemy in dead_enemies:
        enemy.remove(dead_enemy)
    for x in range(len(enemy)):
        enemy[x].name = f'Przeciwnik {x + 1}'


enemies = create_enemies()
guns = [Weapon('1', 'Hitscan'), Weapon('2', 'Projectile'), Weapon('3', 'Area')]

while len(enemies) > 0:
    print('Przeciwnicy:'+ '\n')
    enemy_names = [enemy.name for enemy in enemies]
    print(''.join([f"{name: <25}" for name in enemy_names]))

    enemy_hps = [f"HP {enemy.hp: <22}" for enemy in enemies]
    print(''.join(enemy_hps))

    enemy_armors = [f"Armor {enemy.armor: <19}" for enemy in enemies]
    print(''.join(enemy_armors) + '\n')
    print('Bronie do wyboru:')
    weapon_info = [f"Broń {gun.name: <20}Typ {gun.weapon_type}" for gun in guns]
    print('\n'.join(weapon_info) + '\n')
    print('Wybierz numer broni której chcesz użyć:')
    weapon_number = input()
    print('Wybierz numer przeciwnika którego chcesz zaatakować:')
    enemy_number = input()
    deal_dmg(guns[int(weapon_number) - 1], enemies, int(enemy_number))
print('Wszyscy przeciwnicy pokonani.')


