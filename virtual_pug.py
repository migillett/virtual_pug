#!/usr/bin/env python3

# This is a program meant to be a fun, digital pet
# COPYRIGHT MICHAEL GILLETT 2019
# Compatible with Python 3

import json
import os
from sys import exit

from assets.functions import *

save_game = './savegame.json'

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
        pet['name'] = str(input('Name: ')).capitalize()

        while True:
            print(f'\nIs {pet["name"]} a boy or a girl?')
            choice = input('Input: ')

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
        accident(pet)
        fatass(pet)
        level_up(pet)
        multiplier(pet)
        
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
        user_input = input('Input: ')

        choice = []
        try:
            choice.append(int(user_input))
        except ValueError:
            choice = user_input.split(' ')

        # FEED DOG
        if bool(set(choice)&set([1, 'feed', 'food'])):
            food(pet)

        # GIVE DOG WATER
        elif bool(set(choice)&set([2, 'water'])):
            water(pet)

        # PUT DOG TO BED
        elif bool(set(choice)&set([3, 'bed', 'sleep'])):
            bed(pet)

        # CHECK pet_vitals
        elif bool(set(choice)&set([4, 'vitals', 'health'])):
            vitals(pet)

        # HEAL DOG
        elif bool(set(choice)&set([5, 'heal', 'vet'])):
            heal(pet)

        # TAKE DOG FOR WALK
        elif bool(set(choice)&set([6, 'walk'])):
            walk(pet)

        # GIVE DOG TOY
        elif bool(set(choice)&set([7, 'play', 'toy'])):
            give_toy(pet)

        # EXIT
        elif bool(set(choice)&set([8, 'save', 'quit'])):
            with open(save_game, 'w') as save:
                json.dump(pet, save)
            exit('\nGoodbye\n')
            
        # ELSE
        else:
            error()


if __name__ == '__main__':
    main()
