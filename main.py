import requests
from user_weapon import weapon
from enemy import enemy
from player import player
import random

BASE_URL = "https://www.dnd5eapi.co/api/2014/"
weapon
enemy 
player

while (True):
    print("1. Goblin 2. Bandit\n")
    monster = input("Which monster would you like to fight? (Choose One)\n")
    if monster.lower() == "goblin" or monster.lower() == "bandit":
        request = requests.get(BASE_URL + "monsters/" + monster).json()
        enemy = enemy(**request)
        break      
    else:
        print("Please enter one of the two choices...\n")
        
while (True):
    print("1. Spell (Fire-bolt) 2.Weapon (Battle-Axe)\n")
    choice = input("Make your choice...\n")
    if choice.lower() == "spell":
        print("Fire-bolt has been added to your inventory!")
        request = requests.get(BASE_URL + "spells/" + "fire-bolt").json()
        weapon = weapon(**request)
        break
    elif choice.lower() == "weapon":
        print("Battle-Axe has been added to your inventory!")
        request = requests.get(BASE_URL + "equipment/" + "battleaxe").json()
        weapon = weapon(**request)
        break
    else:
        print("Please enter 'spell' or 'weapon'...")


print(f"{weapon.name} {weapon.damage.damage_dice}")
player = player(10, 15, weapon.damage.damage_dice)

print(f"You are fighting a {enemy.name}, which does {enemy.actions[0].damage[0].damage_dice} damage. You are using the {weapon.name}, which does {weapon.damage.damage_dice} damage")
while(True): 
    print("What would you like to do?\n")
    choice = input("1. Attack (type 'attack')")
    if choice.lower() == "attack":
        hit_dice = random.randrange(1, 21)
        if hit_dice > enemy.armor_class[0].value:
            print(F"You rolled a {hit_dice}, you hit the {enemy.name}! You will roll for damage...")
            num_dice, num_sides = player.damage_dice.split('d')
            roll = random.randint(1, num_sides + 1)
            damage = roll * num_dice
            enemy.hit_points -= damage
            print(f"Your total damage was {damage}, the enemy now has {enemy.hit_points} health!")
        else:
            print(f"You rolled a {hit_dice}, you miss the {enemy.name}")


    
