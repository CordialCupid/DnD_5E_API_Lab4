import requests
from user_weapon import weapon
from enemy import enemy
from player import player
from player_spell import player_spell
import random
import os, re, time

BASE_URL = "https://www.dnd5eapi.co/api/2014/"
weapon
enemy 
player

while (True):
    print("1. Goblin 2. Bandit\n")
    monster = int(input("Which monster would you like to fight? (type the number)...\n"))
    if monster == 1:
        request = requests.get(BASE_URL + "monsters/goblin").json()
        enemy = enemy(**request)
        break 
    elif monster == 2:
        request = requests.get(BASE_URL + "monsters/bandit").json()
        enemy = enemy(**request)
        break      
    else:
        print("Please enter one of the two choices...\n")
        
os.system('cls')
while (True):
    print("1. Spell (Fire-bolt) 2.Weapon (Battle-Axe)\n")
    choice = int(input("Make your choice...\n"))
    if choice == 1:
        print("Fire-bolt has been added to your inventory!")
        request = requests.get(BASE_URL + "spells/fire-bolt").json()
        weapon = player_spell(**request)
        break
    elif choice == 2:
        print("Battle-Axe has been added to your inventory!")
        request = requests.get(BASE_URL + "equipment/battleaxe").json()
        weapon = weapon(**request)
        break
    else:
        os.system('cls')
        print("Please enter '1' or '2'...")

if weapon.name == "Fire Bolt":
    player = player(20, 15, weapon.damage.damage_at_character_level["1"])
elif weapon.name == "Battleaxe":
    player = player(20, 15, weapon.damage.damage_dice)

os.system('cls')
print(f"You have {player.hit_points} hp , {player.armor_class} armor class\n")
print(f"You are fighting a {enemy.name}, which does {enemy.actions[0].damage[0].damage_dice} damage. You are using the {weapon.name}, which does {player.damage_dice} damage...\n")

while(True):
    if player.hit_points <= 0:
        os.system('cls')
        print("You are dead! You lost!\n") 
        break
    elif enemy.hit_points <= 0:
        os.system('cls')
        print(f"The enemy {enemy.name} died! You won!\n")
        break
    print("What would you like to do?\n")
    choice = int(input("1. Attack 2. Disengage \n"))
    if choice == 1:
        hit_dice = random.randrange(1, 21)
        if hit_dice >= enemy.armor_class[0].value:
            print(f"You rolled a {hit_dice}, you hit the {enemy.name}! You will roll for damage...\n")
            num_dice, num_sides = map(int,player.damage_dice.split('d'))
            roll = random.randint(1, num_sides + 1)
            damage = roll * num_dice
            enemy.hit_points -= damage
            if enemy.hit_points > 0:
                print(f"Your total damage was {damage}, the enemy now has {enemy.hit_points} health!\n")
            else:
                print(f"You hit the {enemy.name} for {damage} damage and killed it! You won!\n")
                break
        else:
            print(f"You rolled a {hit_dice}, you miss the {enemy.name}\n")
    elif choice == 2:
        print("You run away!\n")
        break
    print(f"The {enemy.name} will attack!\n")
    time.sleep(2)
    enemy_hit_dice = random.randrange(1, 21)
    if enemy_hit_dice >= player.armor_class:
        print(f"The enemy rolled a {enemy_hit_dice}, they hit you! They will now roll for damage...\n")
        match = re.match(r"(\d+)d(\d+)([+-]\d+)?", enemy.actions[0].damage[0].damage_dice)
        enemy_num_dice = int(match.group(1))
        enemy_num_sides = int(match.group(2))
        enemy_modifier = int(match.group(3)) if match.group(3) else 0
        enemy_roll = random.randint(1, enemy_num_sides + 1)
        enemy_damage = (enemy_roll * enemy_num_dice) + enemy_modifier
        player.hit_points -= enemy_damage
        print(f"The {enemy.name} did {enemy_damage} damage to you, you now have {player.hit_points} hp\n")
    else:
        print(f"The {enemy.name} rolled a {enemy_hit_dice} and missed!\n")


    
