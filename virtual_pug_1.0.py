# This is a program meant to be a fun, digital pet
# COPYRIGHT MICHAEL GILLETT 2019
# Compatible with Python 3

import time
import random
from random import choice

# CHARACTER DICTIONARIES

pet = {
    'name': '',
    'sex': '',
    'pronoun': '',
    'hungry': 0,
    'thirst': True,
    'weight': 18.5,
    'tired': False,
    'sleep': False,
    'lvl': 1,
    'hp': 10,
    'max_hp': 10,
    'age': 8,
    'xp': 0,
    'multiplier': 4,
    'level_up': 10,
    'sick': False,
    'ap': [5, 10],
    'poop': False,
    'pee': False,
    'bored': True,
    'toy': 0
}

enemy_names = ['Squirrel', 'Frog', 'Toad']

enemy = {
    'hp': 10,
    'max_hp': 10,
    'ap': [4, 8],
    'multiplier': 1
}

# PET PICTURES

picture = ('\n'
           ' /\___/\\\n'
           '\n'
           '(  O  O )\n'
           ' (  T  )\n')
happy = ('\n'
         ' /\___/\\\n'
         '\n'
         '(  ^  ^ )\n'
         ' (  T  )\n')
sleep = ('\n'
         ' /\___/\\\n'
         '           zZzZzZzZ\n'
         '(  -  - )\n'
         ' (  T  )\n')
confusion = ('\n   ?\n'
             ' /\___/\\\n'
             '   _  -    \n'
             '(  0  0 )\n'
             ' (  T  )\n')
ko = ('\n'
      ' /\___/\\\n'
      '\n'
      '(  x  x )\n'
      ' (  T  )\n')
angry = ('\n'
         ' /\___/\\\n'
         '   \  /\n'
         '(  O  O )\n'
         ' (  T  )\n')
attacking = ('\n'
             ' /\___/\\\n'
             '   \  /\n'
             '(  O  O )\n'
             ' (  T  )  *bork*\n')
wow = ('    !\n'
       ' /\___/\\\n'
       '   ^  ^\n'
       '(  O  O )\n'
       ' (  T  )\n')
oops = ('\n'
        ' /\___/\\\n'
        '   /  \\\n'
        '(  O  O )\n'
        ' (  T  )\n')

# MENU DICTIONARIES

main_menu = ('''
--------------------------
What would you like to do?
--------------------------
1. Give {0} food
2. Give {0} water
3. Wake {0} or put {0} to bed
4. Check {0}\'s vitals
5. Heal {0}
6. Take {0} for a walk
7. Give {0} a toy
8. Exit
 ''')

attack_menu = ('''
--------------------------
What would you like to do?
--------------------------
1. Attack {0}
2. Heal {1}
3. Flee
 ''')

toy_menu = ('''
------------------------------------------
Which toy would you like to give your pet?
------------------------------------------
1. Dog bone
2. Tennis ball
3. Squeaker toy
4. Return to main menu
 ''')


# ESSENTIAL GAME FUNCTIONS


def press_enter():
    input('\nPress enter to continue.')


def error():
    print('\nPlease enter an integer from the menu.')
    press_enter()


def pet_heal():
    print(happy, '\nYou give {0} a medkit. {0} is now at full health.'.format(pet['name']))
    pet['hp'] = pet['max_hp']
    press_enter()


def pet_asleep():
    print(sleep, '\n{0} is sleeping. You will need to wake {0} up first.'.format(pet['name']))


def level_up():
    if pet['xp'] >= pet['level_up']:
        pet['lvl'] += 1
        pet['max_hp'] = round(pet['max_hp'] * 1.5)
        pet['hp'] = pet['max_hp']
        pet['xp'] = pet['xp'] - pet['level_up']
        pet['level_up'] = round(pet['level_up'] * 2)
        print(happy, '''
{0} has gained a level!
{0} is now level {1}!
XP needed for next level: {2}'''.format(pet['name'], pet['lvl'], pet['level_up']))
        press_enter()


def walking():
    pet['weight'] -= 0.5
    for x in range(3):
        print('\nWalking...')
        time.sleep(1)
        pet['xp'] += pet['multiplier'] * 1
        level_up()


def pet_ko():
    if pet['hp'] <= 0:
        print(ko, '\noh no! {0} took too much damage and passed out!'.format(pet['name']))


def accident():
    if not pet['thirst']:
        pee_inside = random.randint(0, 4)
        if pee_inside == 4:
            print(oops, '\nOh no! {0} peed inside! Better clean that up and take {0} outside.'.format(pet['name']))
            print('Press enter to clean up the mess.')
            input()


def fatass():
    if pet['weight'] < 20 and pet['sick']:
        print(happy, '\nGood job! {0} is back down to a healthy weight and is feeling better.'.format(pet['name']))
        pet['sick'] = False
    elif pet['weight'] >= 20:
        print(oops, '''
{0} has gained some pounds and is starting to have breathing issues.
Looks like it\'s time for a diet!
{0} won\'t be able to level as quickly anymore.'''.format(pet['name']))
        pet['sick'] = True
        press_enter()
    elif pet['weight'] >= 21:
        pet['hp'] -= 5
        pet['sick'] = True
        print(ko, '''
{0} has gained too much weight!
{1} max HP has decreased.'''.format(pet['name'], pet['pronoun']))
        press_enter()


def multiplier():
    if pet['sick']:
        pet['multiplier'] -= 2
    else:
        pet['multiplier'] = 4


# MENU OPTIONS DICTIONARIES

def vitals():
    print('''
--------------------
     PET VITALS
--------------------

{0} | Age: {1}
Sex: {2}
HP: {3} of {4}
Weight: {5}
Level: {6}
Experience points: {7}
XP needed to level up: {8}
'''.format(pet['name'], pet['age'], pet['sex'], pet['hp'], pet['max_hp'], pet['weight'], pet['lvl'], pet['xp'],
           pet['level_up']))
    if pet['sick']:
        print('\n{0} has having breathing issues due to {1} weight.'.format(pet['name'], pet['pronoun']))
    elif pet['poop'] or pet['pee']:
        print('Looks like {0} might need to go to the bathroom.'.format(pet['name']))
        press_enter()
    else:
        press_enter()


# FEED PET

def food():
    if pet['sleep']:
        pet_asleep()
        press_enter()
    elif pet['hungry'] < 3:
        pet['hungry'] += 1
        xp_gain = pet['multiplier'] * 2
        pet['xp'] += xp_gain
        pet['weight'] += 0.5
        pet['hp'] = pet['max_hp']
        pet['poop'] = True
        pet['bored'] = True
        print('''
{0}\n{1} enjoyed {2} meal and earned {3} XP!'''.format(happy, pet['name'], pet['pronoun'], xp_gain))
        press_enter()
    elif pet['hungry'] >= 3:
        print(ko, '''
 You fed {0} too much.
 {0} just threw up everywhere.
 {0} lost 5 hp because of your negligence.
'''.format(pet['name']))
        pet['hp'] -= 5
        pet['hungry'] = 0
        pet['weight'] -= 0.5
        press_enter()


# GIVE PET WATER

def water():
    if pet['sleep']:
        pet_asleep()
        press_enter()
    elif pet['thirst']:
        pet['thirst'] = False
        pet['pee'] = True
        xp_gain = pet['multiplier'] * 2
        pet['xp'] += xp_gain
        print(happy, '\n{0} is no longer thirsty.\n{0} earned {1} XP!'.format(pet['name'], xp_gain))
        press_enter()
    elif not pet['thirst']:
        print(angry, '\n{0} is not thirsty right now. Try again later.\n'.format(pet['name']))
        press_enter()


# WAKE/SLEEP PET

def bed():
    if pet['sleep']:
        wakeup = random.randint(1, 4)
        if wakeup >= 2:
            pet['sleep'] = False
            pet['tired'] = False
            pet['bored'] = True
            print(picture, '\n{0} is groggy, but awake.'.format(pet['name']))
            press_enter()
        else:
            print('''
 Looks like {0} is sleeping too hard to wake up right now.
 {0} might need some more coercion.'''.format(pet['name']))
            press_enter()
    elif not pet['sleep'] and pet['tired']:
        pet['tired'] = False
        pet['sleep'] = True
        print(sleep)
        press_enter()
    elif not pet['sleep'] and not pet['tired']:
        print(happy, '\n{0} is not tired right now. Maybe take {0} for a walk?\n'.format(pet['name']))
        press_enter()

# ATTACK

def attack():
    print('\n{0} attacks the {1}'.format(pet['name'], current_enemy))
    attack_dmg = randint(pet['ap'])
    enemy['hp'] = enemy['hp'] - attack_dmg
    print('\n{0} did {1} damage!'.format(attack_point))

# HEAL PET

def heal():
    if pet['sleep']:
        pet_asleep()
        press_enter()
    else:
        pet_heal()


# GO HOME

def go_home():
    print('\nYou and {0} made it back home.'.format(pet['name']))
    press_enter()
    pet['hungry'] -= 1
    pet['thirst'] = True
    pet['tired'] = True


# LOOT WHILE WALKING

def loot():
    loot_probability = random.randint(0, 9)
    if loot_probability == 1 and pet['multiplier'] < 8:
        print(wow, '\nWhat\'s this? Looks like {0} found something.'.format(pet['name']))
        input('\nPress enter to open...')
        print(happy, '\nYou found a golden dog collar! You now gain 2x as much experience from all actions.')
        pet['multiplier'] = 8
        press_enter()
    elif loot_probability == 2:
        print('\nLooks like {0} found something.'.format(pet['name']))
        input('\nPress enter to open...')
        print(happy, '\nYou found a soggy tennis ball! What luck. {0} gained 15 xp.'.format(pet['name']))
        press_enter()
        pet['xp'] += 15


# WALK PET

def walk():
    if pet['sleep']:
        pet_asleep()
        press_enter()
    else:
        print('\nTaking {0} for a walk.'.format(pet['name']))
        press_enter()
        while True:
            if pet['pee'] or pet['poop']:
                walking()
                print('\n{0} is stopping to use the bathroom.'.format(pet['name']))
                press_enter()
                xp_gain = pet['multiplier'] * 2
                pet['xp'] += xp_gain
                print('\n{0} feels much better now and gained {1} XP!'.format(pet['name'], xp_gain))
                pet['pee'] = False
                pet['poop'] = False
                walking()
            else:
                walking()
            loot()
            print('\nWould you like to keep walking with {0}?'.format(pet['name']))
            continue_walking = int(input('1. Yes\n2. No\n\nInput: '))
            if continue_walking == 1:
                print('\nYou and {0} keep walking.'.format(pet['name']))
                walking()
            elif continue_walking == 2:
                go_home()
                break
            else:
                error()


# GIVE PET TOY

def give_toy():
    while True:
        if pet['sleep']:
            pet_asleep()
            press_enter()
            break
        elif pet['tired']:
            print('\n{0} is too tired to play with a toy right now. Maybe later.'.format(pet['name']))
            press_enter()
            break
        else:
            print(toy_menu)
            pet['toy'] = input(' Input: ')
            try:
                pet['toy'] = int(pet['toy'])
            except ValueError:
                pass
            pet['bored'] = False
            if pet['toy'] == 1:
                print(happy, '\nYou give {0} a dog bone. This should occupy {0} for a while.'.format(pet['name']))
                press_enter()
                break
            elif pet['toy'] == 2:
                print(confusion, '\n{0} doesn\'t seem to understand fetch.'.format(pet['name']))
                press_enter()
                break
            elif pet['toy'] == 3:
                print(happy, '\n{0} seems to really enjoy playing with it.'.format(pet['name'], pet['pronoun']))
                press_enter()
                break
            elif pet['toy'] == 4:
                break
            else:
                error()


# PROGRAM STARTS HERE

print('''
-------------------------------------
      Welcome to Pug Simulator!
-------------------------------------

 What is your pug's name?''')
pet['name'] = input(' Name: ')
while True:
    print('\nIs your pet male or female?\n1. Male\n2. Female\n')
    choice = input(' Input: ')
    try:
        choice = int(choice)
    except ValueError:
        error()
    if choice == 1:
        pet['sex'] = 'male'
        pet['pronoun'] = 'his'
        break
    elif choice == 2:
        pet['sex'] = 'female'
        pet['pronoun'] = 'her'
        break
    else:
        error()
while True:
    accident()
    fatass()
    level_up()
    multiplier()
    print(main_menu.format(pet['name']))
    choice = input(' Input: ')
    try:
        choice = int(choice)
    except ValueError:
        error()
    # FEED DOG
    if choice == 1:
        food()
    # GIVE DOG WATER
    elif choice == 2:
        water()
    # PUT DOG TO BED
    elif choice == 3:
        bed()
    # CHECK pet_vitals
    elif choice == 4:
        vitals()
    # HEAL DOG
    elif choice == 5:
        heal()
    # TAKE DOG FOR WALK
    elif choice == 6:
        walk()
    # GIVE DOG TOY
    elif choice == 7:
        give_toy()
    # EXIT
    elif choice == 8:
        print('\n\nGoodbye\n\n')
        break
    # PRINT DICTIONARY FOR DEBUG
    elif choice == 100:
        print(pet)
    # ELSE
    else:
        error()
