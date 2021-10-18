#!/usr/bin/env python3

# This is a program meant to be a fun, digital pet
# COPYRIGHT MICHAEL GILLETT 2019
# Compatible with Python 3

import time
import random
import json
import os
from sys import exit

save_game = 'game_save.json'

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

# enemy combat removed for now saving for later

# enemy_names = ['Squirrel', 'Frog', 'Toad']

#enemy = {
#    'hp': 10,
#    'max_hp': 10,
#    'ap': [4, 8],
#    'multiplier': 1
#}

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
    print('\nUnrecognized input. Please try again.')
    press_enter()


def pet_heal():
    print(happy, f'\nYou took {pet["name"]} to the vet. {pet["name"]} is now back at full health!')
    pet['hp'] = pet['max_hp']
    press_enter()


def pet_asleep():
    print(sleep, f'\n{pet["name"]} is sleeping. You will need to wake {pet["name"]} up first.')


def level_up():
    if pet['xp'] >= pet['level_up']:
        pet['lvl'] += 1
        pet['max_hp'] = round(pet['max_hp'] * 1.5)
        pet['hp'] = pet['max_hp']
        pet['xp'] = pet['xp'] - pet['level_up']
        pet['level_up'] = round(pet['level_up'] * 2)
        print(happy, f'''
{pet["name"]} has gained a level!
{pet["name"]} is now level {pet["lvl"]}!
XP needed for next level: {pet["level_up"]}''')
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
        print(ko, f'\noh no! {pet["name"]} took too much damage and passed out!')


def accident():
    if not pet['thirst']:
        pee_inside = random.randint(0, 4)
        if pee_inside == 4:
            print(oops, f'\nOh no! {pet["name"]} peed inside! Better clean that up and take {pet["name"]} outside.')
            print('Press enter to clean up the mess.')
            input()


def fatass():
    if pet['weight'] < 20 and pet['sick']:
        print(happy, f'\nGood job! {pet["name"]} is back down to a healthy weight and is feeling better.')
        pet['sick'] = False
    elif pet['weight'] >= 20:
        print(oops, f'''
{pet["name"]} has gained some pounds and is starting to have breathing issues.
Looks like it\'s time for a diet!
{pet["name"]} won\'t be able to level as quickly anymore.''')
        pet['sick'] = True
        press_enter()
    elif pet['weight'] >= 21:
        pet['hp'] -= 5
        pet['sick'] = True
        print(ko, f'''
{pet["name"]} has gained too much weight!
{pet["pronoun"]} max HP has decreased.''')
        press_enter()


def multiplier():
    if pet['sick']:
        pet['multiplier'] -= 2
    else:
        pet['multiplier'] = 4


# MENU OPTIONS DICTIONARIES

def vitals():
    print(f'''
--------------------
     PET VITALS
--------------------

{pet["name"]} | Age: {pet["age"]}
Sex: {pet["sex"]}
HP: {pet["hp"]} of {pet["max_hp"]}
Weight: {pet["weight"]}
Level: {pet["lvl"]}
Experience points: {pet["xp"]}
XP needed to level up: {pet["level_up"]}
''')
    if pet['sick']:
        print(f'\n{pet["name"]} has having breathing issues due to {pet["pronoun"]} weight.')
    elif pet['poop'] or pet['pee']:
        print(f'Looks like {pet["name"]} might need to go to the bathroom.')
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
        print(f'''
{happy}\n{pet["name"]} enjoyed {pet["pronoun"]} meal and earned {xp_gain} XP!''')
        press_enter()
    elif pet['hungry'] >= 3:
        print(ko, f'''
 You fed {pet["name"]} too much.
 {pet["name"]} just threw up everywhere.
 {pet["name"]} lost 5 hp because of your negligence.
''')
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
        print(happy, f'\n{pet["name"]} is no longer thirsty.\n{pet["name"]} earned {xp_gain} XP!')
        press_enter()
    elif not pet['thirst']:
        print(angry, f'\n{pet["name"]} is not thirsty right now. Try again later.\n')
        press_enter()


# WAKE/SLEEP PET

def bed():
    if pet['sleep']:
        wakeup = random.randint(1, 4)
        if wakeup >= 2:
            pet['sleep'] = False
            pet['tired'] = False
            pet['bored'] = True
            print(picture, f'\n{pet["name"]} is groggy, but awake.')
            press_enter()
        else:
            print(f'''
 Looks like {pet["name"]} is sleeping too hard to wake up right now.
 {pet["name"]} might need some more coercion.''')
            press_enter()
    elif not pet['sleep'] and pet['tired']:
        pet['tired'] = False
        pet['sleep'] = True
        print(sleep)
        press_enter()
    elif not pet['sleep'] and not pet['tired']:
        print(happy, f'\n{pet["name"]} is not tired right now. Maybe take {pet["name"]} for a walk?\n')
        press_enter()


# HEAL PET

def heal():
    if pet['sleep']:
        pet_asleep()
        press_enter()
    if pet['hp'] < pet['max_hp']:
        pet_heal()
    else:
        print('{0} is already at full health and does not need to to go the Veterinarian.')
        press_enter()


# GO HOME

def go_home():
    print(f'\nYou and {pet["name"]} made it back home.')
    press_enter()
    pet['hungry'] -= 1
    pet['thirst'] = True
    pet['tired'] = True


# LOOT WHILE WALKING

def loot():
    loot_probability = random.randint(0, 9)
    if loot_probability == 1 and pet['multiplier'] < 8:
        print(wow, f'\nWhat\'s this? Looks like {pet["name"]} found something.')
        input('\nPress enter to open...')
        print(happy, '\nYou found a golden dog collar! You now gain 2x as much experience from all actions.')
        pet['multiplier'] = 8
        press_enter()
    elif loot_probability == 2:
        print(f'\nLooks like {pet["name"]} found something.')
        input('\nPress enter to open...')
        print(happy, f'\nYou found a soggy tennis ball! What luck. {pet["name"]} gained 15 xp.')
        press_enter()
        pet['xp'] += 15


# WALK PET

def walk():
    if pet['sleep']:
        pet_asleep()
        press_enter()
    else:
        print(f'\nTaking {pet["name"]} for a walk.')
        press_enter()
        while True:
            if pet['pee'] or pet['poop']:
                walking()
                print(f'\n{pet["name"]} is stopping to use the bathroom.')
                press_enter()
                xp_gain = pet['multiplier'] * 2
                pet['xp'] += xp_gain
                print(f'\n{pet["name"]} feels much better now and gained {xp_gain} XP!')
                pet['pee'] = False
                pet['poop'] = False
                walking()
            else:
                walking()

            loot()

            print(f'\nWould you like to keep walking with {pet["name"]}?')
            continue_walking = str(input('Yes or no?: ')).lower()

            if continue_walking in ['yes', 'keep walking', 'keep']:
                print(f'\nYou and {pet["name"]} keep walking.')
                walking()
                
            elif continue_walking in ['no', 'go home', 'home', 'stop']:
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
            print(f'\n{pet["name"]} is too tired to play with a toy right now. Maybe later.')
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
                print(happy, f'\nYou give {pet["name"]} a dog bone. This should occupy {pet["name"]} for a while.')
                press_enter()
                break
            elif pet['toy'] == 2:
                print(confusion, f'\n{pet["name"]} doesn\'t seem to understand fetch.')
                press_enter()
                break
            elif pet['toy'] == 3:
                print(happy, f'\n{pet["name"]} seems to really enjoy playing with it.')
                press_enter()
                break
            elif pet['toy'] == 4:
                break
            else:
                error()


# PROGRAM STARTS HERE
def main():
    global pet
    # If a save game exists, allow player to load it
    if os.path.exists(save_game):
        while True:
            load_game_select = input('\nWould you like to load a previous save? (Yes/No):')
            try:
                load_game_select = str(load_game_select.lower())
            except ValueError:
                error()

            if load_game_select in ['y', 'yes']:
                with open(save_game, 'r') as save:
                    print('Save game loaded, welcome back!')
                    pet = json.load(save)
                    vitals()
                break
            elif load_game_select in ['n', 'no']:
                break
            else:
                error()

    if not pet['name']:
        print('''
-------------------------------------
        Welcome to Pug Simulator!
-------------------------------------
        
What is your pug's name?''')
        pet['name'] = input(' Name: ')
        while True:
            print(f'\nIs {pet["name"]} a boy or a girl?')
            choice = input(' Input: ')

            try:
                choice = int(choice)
            except ValueError:
                choice = str(choice).lower()

            if choice in [1, 'male', 'boy']:
                pet['sex'] = 'male'
                pet['pronoun'] = 'his'
                break

            elif choice in [2, 'female', 'girl']:
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
        
        main_menu = (f'''
--------------------------
What would you like to do?
--------------------------
1. Give {pet["name"]} food
2. Give {pet["name"]} water
3. Wake {pet["name"]} or put {pet["name"]} to bed
4. Check {pet["name"]}'s vitals
5. Take {pet["name"]} to the vet's office
6. Take {pet["name"]} for a walk
7. Give {pet["name"]} a toy
8. Exit
 ''')
        print(main_menu)
        user_input = input(' Input: ')

        choice = []
        try:
            choice.append(int(user_input))
        except ValueError:
            choice = user_input.split(' ')

        # FEED DOG
        if bool(set(choice)&set([1, 'feed', 'food'])):
            food()
        # GIVE DOG WATER
        elif bool(set(choice)&set([2, 'water'])):
            water()
        # PUT DOG TO BED
        elif bool(set(choice)&set([3, 'bed', 'sleep'])):
            bed()
        # CHECK pet_vitals
        elif bool(set(choice)&set([4, 'vitals', 'health'])):
            vitals()
        # HEAL DOG
        elif bool(set(choice)&set([5, 'heal', 'vet'])):
            heal()
        # TAKE DOG FOR WALK
        elif bool(set(choice)&set([6, 'walk'])):
            walk()
        # GIVE DOG TOY
        elif bool(set(choice)&set([7, 'play', 'toy'])):
            give_toy()
        # EXIT
        elif bool(set(choice)&set([8, 'save', 'quit'])):
            with open(save_game, 'w') as save:
                json.dump(pet, save)
            exit('\n\nGoodbye\n\n')
        # PRINT DICTIONARY FOR DEBUG
        elif choice == 100:
            print(pet)
        # ELSE
        else:
            error()


if __name__ == '__main__':
    main()
