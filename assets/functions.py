from .pet_emoji import *
import time
from random import randint

# ESSENTIAL GAME FUNCTIONS
def press_enter():
    input('\nPress enter to continue.')


def error():
    print('\nUnrecognized input. Please try again.')
    press_enter()


def pet_heal(pet):
    print(happy, f'\nYou took {pet["name"]} to the vet. {pet["name"]} is now back at full health!')
    pet['hp'] = pet['max_hp']
    press_enter()


def pet_asleep(pet):
    print(sleep, f'\n{pet["name"]} is sleeping. You will need to wake {pet["name"]} up first.')


def level_up(pet):
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


def walking(pet):
    pet['weight'] -= 0.5
    for x in range(3):
        print('\nWalking...')
        time.sleep(1)
        pet['xp'] += pet['multiplier'] * 1
        level_up(pet)


def pet_ko(pet):
    if pet['hp'] <= 0:
        print(ko, f'\noh no! {pet["name"]} took too much damage and passed out!')


def accident(pet):
    if not pet['thirst']:
        pee_inside = randint(0, 4)

        if pee_inside == 4:
            print(oops, f'\nOh no! {pet["name"]} peed inside! Better clean that up and take {pet["name"]} outside.')
            print('Press enter to clean up the mess.')
            input()


def fatass(pet):
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


def multiplier(pet):
    if pet['sick']:
        pet['multiplier'] -= 2
    else:
        pet['multiplier'] = 4


# MENU OPTIONS DICTIONARIES

def vitals(pet):
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
def food(pet):
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
def water(pet):
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
def bed(pet):
    if pet['sleep']:
        wakeup = randint(1, 4)
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
def heal(pet):
    if pet['sleep']:
        pet_asleep()
        press_enter()
    if pet['hp'] < pet['max_hp']:
        pet_heal()
    else:
        print(f'{pet["name"]} is already at full health and does not need to to go the Veterinarian.')
        press_enter()


# GO HOME
def go_home(pet):
    print(f'\nYou and {pet["name"]} made it back home.')
    press_enter()
    pet['hungry'] -= 1
    pet['thirst'] = True
    pet['tired'] = True


# LOOT WHILE WALKING
def loot(pet):
    loot_probability = randint(0, 9)
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
def walk(pet):
    if pet['sleep']:
        pet_asleep()
        press_enter()

    else:
        print(f'\nTaking {pet["name"]} for a walk.')
        press_enter()
        if pet['pee'] or pet['poop']:
            walking(pet)
            print(f'\n{pet["name"]} is stopping to use the bathroom.')
            press_enter()
            xp_gain = pet['multiplier'] * 2
            pet['xp'] += xp_gain
            print(f'\n{pet["name"]} feels much better now and gained {xp_gain} XP!')
            pet['pee'] = False
            pet['poop'] = False
            walking(pet)

        else:
            walking(pet)
            loot(pet)

            while True:
                print(f'\nWould you like to keep walking with {pet["name"]}?')
                choice = str(input('Yes or no?: ')).lower()

                if choice in ['y', 'yes', 'continue', 'keep']:
                    print(f'\nYou and {pet["name"]} keep walking.')
                    walking(pet)
                    
                elif choice in ['n', 'no', 'return', 'home', 'stop']:
                    go_home(pet)
                    break

                else:
                    error()


# GIVE PET TOY
def give_toy(pet):
    while True:
        if pet['sleep']:
            pet_asleep(pet)
            press_enter()
            break

        elif pet['tired']:
            print(f'\n{pet["name"]} is too tired to play with a toy right now. Maybe later.')
            press_enter()
            break

        else:
            print('''
------------------------------------------
Which toy would you like to give your pet?
------------------------------------------
 Dog bone
 Tennis ball
 Squeaker toy

 Enter "q" to return to the main menu
 ''')
            user_input = str(input('Input: ')).lower()
            choice = user_input.split(' ')

            pet['bored'] = False

            if bool(set(choice)&set(['bone'])):
                print(happy, f'\nYou give {pet["name"]} a dog bone. This should occupy {pet["name"]} for a while.')
                press_enter()
                break

            elif bool(set(choice)&set(['tennis', 'ball'])):
                print(confusion, f'\n{pet["name"]} doesn\'t seem to understand fetch.')
                press_enter()
                break

            elif bool(set(choice)&set(['squeaker', 'squeaky'])):
                print(happy, f'\n{pet["name"]} seems to really enjoy playing with the squeaker toy.')
                press_enter()
                break

            elif bool(set(choice)&set(['q', 'quit', 'return'])):
                break

            else:
                error()
